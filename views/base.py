from flask import (
        Blueprint,
        render_template,
        send_from_directory,
        redirect,
        request,
        g,
        current_app)
import json
import jwt
from datetime import datetime, timedelta

from models.user import utils as user

views = Blueprint('main', __name__)

#Cette fonction est le point de depart de l'application.
@views.route('/')
def index():
    return render_template('index.html',path={'path':''})

@views.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'username' not in data or 'password' not in data:
        return json.dumps({'status': 'Username and password are required'}), 400

    user.create_or_update_user(data)

    return json.dumps({'status': 'User registered successfully, now log in'}), 201

@views.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'username' not in data or 'password' not in data:
        return json.dumps({'status': 'Username and password are required'}), 400

    user_data = user.check_user(data)

    if user_data is None:
        return json.dumps({'status': 'Invalid username or password'}), 401
    else:
        token = jwt.encode({'user_id': user_data['id'], 'exp':datetime.utcnow() + timedelta(minutes=60)}, current_app.config['SECRET_KEY'], algorithm='HS256')
        return json.dumps({
            'token': token,
            'connection_count': user_data['connection_count'],
            'next_card': user_data['next_card'],
            'next_theft': user_data['next_theft']})