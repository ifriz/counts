import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xc1\xc8\xe8\xcd\x11\xf6\xac\x19X\x7f[\xb3\xf0\xbe~\x0eC\x0f"\'\xce.\xac\xbb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'drink.db')
db = SQLAlchemy(app)

from drinkapp import models, views