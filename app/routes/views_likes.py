from flask_apispec import marshal_with, use_kwargs
from marshmallow import fields

from app import like
from app.business_logic.likes import modify_likes, get_post_likes
from app.schemas import ResponseSchema


# Отображение лайков, поставленных конкретному посту
@like.route('/get_post_likes/<int:post_id>', methods=['GET'])
@marshal_with(ResponseSchema())
def get_post_likes_route(post_id):
    return get_post_likes(post_id)


# Модификация количества лайков
@like.route('/modify_likes/<int:post_id>', methods=['PUT'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs({'action': fields.String()})
def modify_likes_route(post_id, **kwargs):
    return modify_likes(post_id, **kwargs)
