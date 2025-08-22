# PDF Converter - Web App

## Overview

**PDF Converter** is a simple web application that allows users to upload images and convert them into a single PDF file.  
The app is built using **Flask**, **Tailwind (via CDN)**, and **Pillow** for image processing.  

## Features

- **Upload multiple images** and combine them into one PDF.
- **Instant download** after conversion.
- **Responsive design** with Tailwind CSS.
- **Lightweight backend** using Flask.
- **Clean UI** for easy file uploads.

## Technologies Used

- **Frontend:** HTML, Tailwind CSS (CDN)
- **Backend:** Python, Flask
- **Image Processing:** Pillow (PIL)
- **Deployment Ready:** Works locally and on Render/Heroku.

## Installation & Run


# 1. Clone the repository
git clone https://github.com/yourusername/PDF-Converter.git
cd PDF-Converter

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open your browser at
http://127.0.0.1:5000

Project Structure
```bash
PDF-Converter/
│
├── app.py               # Main Flask entry point
├── requirements.txt     # Python dependencies
│
├── website/             # Application package
│   ├── __init__.py      # Flask app factory
│   ├── views.py         # Flask routes
│   ├── pdfy.py          # PDF conversion logic (Pillow)
│   ├── templates/       # HTML templates
│   │   ├── base.html.j2
│   │   ├── home.html.j2
│   │   └── output.html.j2
│   └── static/          # CSS / JS
│       ├── style.css
│       └── index.js
│
└── README.md            # Documentation
```
## Contributing

 1. Fork the repo
 2. Create a new branch
git checkout -b feature-name

 3. Commit your changes
git commit -m "Add feature"

 4. Push to your branch
git push origin feature-name

 5. Open a Pull Request

Deployment (Render)

 1. Push your project to GitHub
 2. On Render, create a new Web Service and connect your repo
 3. Set your Start Command
gunicorn app:app

 4. Add a requirements.txt file if not already included
Flask==3.1.2
pillow==11.3.0
gunicorn==23.0.0

 5. Deploy �

License

This project is licensed under the MIT License.

---
