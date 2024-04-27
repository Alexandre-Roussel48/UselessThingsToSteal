from flask import (
        Blueprint,
        render_template,
        send_from_directory,
        redirect,
        request,
        g,
        session)
import json
from utils import auth

from models.user import utils as user

views = Blueprint('user', __name__)

@views.route('/get_cards', methods=['POST'])
@auth.logged
def register():
    return json.dumps([card.toDict() for card in user.get_inventory(session['user_id'])])

@views.route('/drop', methods=['POST'])
@auth.logged
def drop():
    drop_data = user.drop_card(session['user_id'])
    if drop_data is None:
        return json.dumps({'status': 'Drop unauthorized now'}), 401
    return json.dumps(drop_data)

@views.route('/theft', methods=['POST'])
@auth.logged
def theft():
    return "test"