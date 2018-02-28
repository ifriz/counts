from flask import request, render_template, jsonify, json
from drinkapp import app, db
from .models import User, Drink
from datetime import datetime


@app.route('/api/drink', methods=['POST'])
def add_drink():
    user_id = 0
    if 'user' in request.json.keys():
        user = User.get_user_by_name(request.json['user'])
        if user is not None:
            user_id = user.id
        else:
            user = User(username=request.json['user'])
            db.session.add(user)
    drink = Drink(channel=request.json['channel'], date=datetime.today(), description="", user_id=user_id)
    db.session.add(drink)
    db.session.commit()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/drink/<string:channel_name>', methods=['GET'])
def get_channel(channel_name):
    drinkresult = Drink.get_drink(channel_name)
    # return jsonify(drink)
    return jsonify(json_list=[i.serialize for i in drinkresult.all()])


@app.route('/drink/<string:channel_name>', methods=['GET'])
def show_channel_results(channel_name):
    return render_template('results.html', title="results for {0}".format(channel_name),
                           name = channel_name,
                           count=Drink.get_count(channel_name))


@app.route("/")
def hello():
    return "Hello World!"
