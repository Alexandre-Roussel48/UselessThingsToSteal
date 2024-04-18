from flask import Flask, request, redirect, url_for, g, render_template
from flask_cors import CORS
from peewee import MySQLDatabase, Model
from itsdangerous import (
        TimedSerializer,
        SignatureExpired,
        BadSignature)

import config
import json

app = Flask('__name__')
CORS(app)

app.config.from_pyfile('config.py')

db = MySQLDatabase(
        config.db_name, 
        user=config.db_username,
        password=config.db_password, 
        host=config.db_host,
        port=config.db_port
        )

class BaseModel(Model):
    class Meta:
        database = db

from views import (
    theft,
    inventory,
    user,
    base
)

app.register_blueprint(base.views)

app.register_blueprint(theft.views, url_prefix='/theft')
app.register_blueprint(inventory.views, url_prefix='/inventory')
app.register_blueprint(user.views, url_prefix='/user')


@app.before_request
def _check_user():
    serializer = TimedSerializer(config.SECRET_KEY)

    db.connect(reuse_if_open=True)


@app.teardown_request
def _db_close(exc):
    '''
    Ferme la connection à la base de données une fois que la
    requête a été traitée.
    '''
    if not db.is_closed():
        db.close()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template('index.html', path={'path':path})

if __name__ == '__main__':
    app.run('0.0.0.0')