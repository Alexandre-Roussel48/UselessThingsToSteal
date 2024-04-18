from flask import (
        Blueprint,
        render_template,
        send_from_directory,
        redirect,
        request,
        g)

views = Blueprint('theft', __name__)