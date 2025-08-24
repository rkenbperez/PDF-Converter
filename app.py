from website.main import app, startup_cleanup

# Starts the app

if __name__ == '__main__':
    startup_cleanup()
    app.run(debug=True)