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

views = Blueprint('inventory', __name__)

@views.route('/get_cards', methods=['POST'])
@auth.logged
def register():
    return json.dumps([card.toDict() for card in user.get_inventory(session['user_id'])])