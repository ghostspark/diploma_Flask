from flask import Blueprint

root_blue = Blueprint('root_blue', __name__)

from . import views
