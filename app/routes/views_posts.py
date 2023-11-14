from flask_apispec import use_kwargs, marshal_with

from app import post
from app.business_logic.posts import get_post, create_post, update_post, delete_post
from app.schemas import PostSchema, ResponseSchema


# Отображение постов
@post.route('/posts', methods=['GET'])
@marshal_with(ResponseSchema())
def get_posts_route():
    return get_post()


# Создание поста
@post.route('/create_post', methods=['POST'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs(PostSchema(only=['theme_id', 'content', 'author_id']), apply=True)
def create_post_route(**kwargs):
    return create_post(**kwargs)


# Изменение поста
@post.route('/update_post/<int:post_id>', methods=['PUT'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs(PostSchema(only=['theme_id', 'content', 'author_id']), apply=True)
def update_post_route(post_id, **kwargs):
    return update_post(post_id, **kwargs)


# Удаление поста
@post.route('/delete_post/<int:post_id>', methods=['DELETE'])
@marshal_with(ResponseSchema(exclude=['data']))
def delete_post_route(post_id):
    return delete_post(post_id)
