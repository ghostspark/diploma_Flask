from flask import Blueprint

register_blue = Blueprint('register_blue', __name__, static_folder='./static',
                          template_folder='templates', static_url_path='/')

from . import views
