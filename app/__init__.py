from flask import Blueprint

post = Blueprint('post', __name__, template_folder='templates', static_folder='static')
like = Blueprint('like', __name__, template_folder='templates', static_folder='static')
template = Blueprint('template', __name__, template_folder='templates', static_folder='static')

from .routes import views_likes, views_posts, views_template
