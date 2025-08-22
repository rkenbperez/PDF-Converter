import sys
import os
from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for
from pathlib import Path
import tempfile
import threading
import time

# Add current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfy
from config import EXPORTS_DIR, UPLOADS_DIR

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Needed for flash messages

# Home Route
@app.route('/')
def home():
    return render_template('home.html.j2')

@app.route('/convert', methods=['POST'])
def convert_to_pdf():
    print("Convert route called!")  # Debug
    try:
        # Get uploaded files
        files = request.files.getlist("files")
        print(f"Number of files received: {len(files)}")  # Debug
        
        # Check if files were uploaded
        if not files or len(files) == 0:
            print("No files uploaded")
            flash("No files uploaded!")
            return redirect(url_for('home'))
        
        # Check for valid files (not empty)
        valid_files = [f for f in files if f.filename != '']
        if not valid_files:
            print("No valid files")
            flash("No valid files selected!")
            return redirect(url_for('home'))
        
        print(f"Valid files: {[f.filename for f in valid_files]}")
        
        # Create temporary directory and process files
        with tempfile.TemporaryDirectory(dir=UPLOADS_DIR) as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            print(f"Temp directory: {temp_dir}")
            
            # Save files to temporary directory
            for file in valid_files:
                file_path = temp_dir / file.filename
                file.save(str(file_path))
                print(f"Saved: {file_path}")
            
            # Convert to PDF
            try:
                output_pdf = pdfy.pdf(temp_dir)
                print(f"PDF created: {output_pdf}")
                
                if output_pdf and output_pdf.exists():
                    print("PDF exists, rendering output template")
                    
                    # Clean any old PDFs before creating new ones
                    clean_old_exports()
                    
                    return render_template("output.html.j2", output_pdf=output_pdf.name)
                else:
                    print("PDF was not created or doesn't exist")
                    flash("Failed to create PDF!")
                    return redirect(url_for('home'))
                    
            except Exception as pdf_error:
                print(f"PDF conversion error: {pdf_error}")
                flash(f"Error converting to PDF: {str(pdf_error)}")
                return redirect(url_for('home'))
                
    except Exception as e:
        print(f"General error in convert route: {e}")
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('home'))

def clean_old_exports():
    """Clean exports folder of files older than 5 minutes"""
    try:
        exports_path = Path(EXPORTS_DIR)
        if exports_path.exists():
            current_time = time.time()
            for file_path in exports_path.glob("*.pdf"):
                if file_path.is_file():
                    file_age = current_time - file_path.stat().st_mtime
                    if file_age > 3:
                        file_path.unlink()
                        print(f"Deleted old PDF: {file_path}")
    except Exception as e:
        print(f"Error cleaning old exports: {e}")

@app.route('/download/<path:pdf_name>')
def download_pdf(pdf_name):
    """Route for sharing generated files to users"""
    try:
        pdf_path = Path(EXPORTS_DIR) / pdf_name
        
        # Check if file exists
        if not pdf_path.exists():
            flash("File not found!")
            return redirect(url_for('home'))
        
        # Create the response
        response = send_from_directory(
            EXPORTS_DIR,
            pdf_name,
            mimetype='application/pdf',
            download_name='converted.pdf',
            as_attachment=True
        )
        
        # Delete the file immediately after creating response
        try:
            pdf_path.unlink()
            print(f"Deleted PDF immediately: {pdf_path}")
        except Exception as delete_error:
            print(f"Error deleting file: {delete_error}")
        
        return response
        
    except Exception as e:
        print(f"Download error: {e}")
        flash("Error downloading file!")
        return redirect(url_for('home'))

@app.route('/cleanup')
def cleanup_exports():
    """Manual cleanup of exports folder"""
    try:
        exports_path = Path(EXPORTS_DIR)
        if exports_path.exists():
            deleted_count = 0
            for file_path in exports_path.glob("*.pdf"):
                if file_path.is_file():
                    file_path.unlink()
                    deleted_count += 1
                    print(f"Deleted: {file_path}")
            
            flash(f"Deleted {deleted_count} files from exports folder")
        else:
            flash("Exports folder not found")
            
    except Exception as e:
        print(f"Cleanup error: {e}")
        flash(f"Cleanup failed: {str(e)}")
    
    return redirect(url_for('home'))

def startup_cleanup():
    """Clean exports folder on startup"""
    try:
        exports_path = Path(EXPORTS_DIR)
        if exports_path.exists():
            for file_path in exports_path.glob("*.pdf"):
                if file_path.is_file():
                    file_path.unlink()
                    print(f"Startup cleanup - deleted: {file_path}")
    except Exception as e:
        print(f"Startup cleanup error: {e}")

if __name__ == '__main__':
    print(f"UPLOADS_DIR: {UPLOADS_DIR}")
    print(f"EXPORTS_DIR: {EXPORTS_DIR}")
    
    # Make sure directories exist
    Path(UPLOADS_DIR).mkdir(exist_ok=True)
    Path(EXPORTS_DIR).mkdir(exist_ok=True)
    
    # Clean up any leftover files from previous runs
    startup_cleanup()
    
    # app.run(debug=True)