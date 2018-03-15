from waitress import serve
from drinkapp import app

if __name__ == "main":
    serve(app, listen="*:8080")
