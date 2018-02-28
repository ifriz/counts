from drinkapp import app, db
from drinkapp.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='iantest', password='test'))
    db.session.add(User(username='testuser', password='test'))
    db.session.commit()
    print('Initialized the database')


@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to drop?'):
        db.drop_all()
        print('dropped the database')


if __name__ == '__main__':
    manager.run()
