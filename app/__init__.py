from flask import Blueprint

post = Blueprint('post', __name__, template_folder='templates', static_folder='static')
like = Blueprint('like', __name__, template_folder='templates', static_folder='static')

from .views import posts, likes
