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

 5. Deploy 
