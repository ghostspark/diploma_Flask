from flask import Blueprint

properties_blue = Blueprint('properties_blue', __name__)

from . import views
