from functools import wraps
import json
import jwt
from flask import request, current_app, session

def logged(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return json.dumps({'error': 'Token is missing'}), 401

        try:
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            session['user_id'] = decoded_token['user_id']
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return json.dumps({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return json.dumps({'error': 'Invalid token'}), 401
    return wrapper