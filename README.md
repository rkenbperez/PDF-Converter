PDF Converter - Web App
Overview
PDF Converter is a simple web application that allows users to upload one or more images and convert them into a single PDF document. It features a clean and responsive design with drag-and-drop support, making the process smooth and user-friendly.  The app is built using Python, Flask, TailwindCSS (via CDN), and Pillow for image processing.
Features
Drag & Drop Upload: Easily add files by dragging them into the upload box.
Multiple File Support: Upload multiple images at once.
PDF Conversion: Converts uploaded images into a single PDF file.
Downloadable Output: Get your generated PDF with one click.
Responsive Design: Works well on desktop and mobile devices.
Technologies Used
Frontend: HTML, TailwindCSS (via CDN)
Backend: Python, Flask
Image Processing: Pillow (PIL)
Deployment: Render / Any WSGI-compatible server
Installation
1. Clone the repository:
git clone https://github.com/yourusername/pdf-converter.git cd pdf-converter
2. Create a virtual environment and install dependencies:
python3 -m venv venv source venv/bin/activate   # On Windows: venv\Scripts\activate pip install -r requirements.txt
3. Run the Flask app:
python app.py
4. Open your browser at http://127.0.0.1:5000.
Usage
Drag and drop your images or click to upload.
Press Convert to PDF.
Download the generated PDF file.
Project Structure
PDF-Converter/ │ ├─ app.py                # Flask app entry point ├─ requirements.txt      # Python dependencies ├─ config.py             # Config for exports/uploads directories │ ├─ website/ │   ├─ __init__.py       # App factory │   ├─ views.py          # Routes and logic │   ├─ pdfy.py           # PDF conversion logic │   ├─ templates/        # Jinja2 HTML templates │   │   ├─ base.html.j2 │   │   └─ home.html.j2 │   └─ static/           # CSS and JS files │       ├─ style.css │       └─ index.js 
