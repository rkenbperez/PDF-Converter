# PDF-Converter
A simple web application built with Flask, TailwindCSS (CDN), and Pillow that allows users to upload multiple image files (PNG, JPG, etc.) and convert them into a single PDF.
🚀 Features
- Upload one or more images
- Convert images into a single PDF file
- Download the generated PDF instantly
- Responsive UI styled with TailwindCSS (CDN)
- Lightweight and easy to deploy
🛠️ Tech Stack
- Backend: Flask
- Frontend: TailwindCSS (CDN)
- Image Processing: Pillow
📂 Project Structure

PDF-Converter/
│── app.py
│── requirements.txt
│── config.py
│── website/
│   ├── __init__.py
│   ├── views.py
│   ├── pdfy.py
│   └── templates/
│       ├── base.html.j2
│       ├── home.html.j2
│       └── output.html.j2
│── static/
│   └── index.js

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/PDF-Converter.git
cd PDF-Converter
2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ Usage
1. Run the Flask app:
python app.py
2. Open your browser and go to:
http://127.0.0.1:5000
3. Upload your images → Click Convert to PDF → Download the generated PDF
📦 Deployment
For deployment on platforms like Render or Heroku:
1. Add gunicorn to requirements.txt
gunicorn
2. Create a file named Procfile in the root folder with this content:
web: gunicorn app:app
3. Push to your repository and deploy 🚀
📝 License
This project is licensed under the MIT License.
