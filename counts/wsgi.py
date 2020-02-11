from waitress import serve
from counts import app

if __name__ == "main":
    serve(app, listen="*:8080")
