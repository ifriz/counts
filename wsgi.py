from waitress import serve
from counts import app

if __name__ == '__main__':
    print('\x1b[6;30;42m' + 'starting wsgi server' + '\x1b[0m')
    serve(app, listen="*:8080")
