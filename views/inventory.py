from flask import (
        Blueprint,
        render_template,
        send_from_directory,
        redirect,
        request,
        g)

views = Blueprint('inventory', __name__)