from app import app

# Render y Gunicorn usan esta variable
application = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
