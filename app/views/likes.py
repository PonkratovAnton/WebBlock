from flask_apispec import marshal_with, use_kwargs
from marshmallow import fields

from app import like
from app.database import session
from app.models import Post
from app.schemas import ResponseSchema, PostSchema, success_response, not_found_response, error_response


# Отображение лайков, поставленных конкретному посту
@like.route('/get_post_likes/<int:post_id>', methods=['GET'])
@marshal_with(ResponseSchema())
def get_post_likes(post_id):
    try:
        with session.begin_nested():
            like = PostSchema().dump(session.query(Post.likes).filter(Post.post_id == post_id).first())
            if not like:
                    return not_found_response('No posts with this id')
        return success_response(like)
    except Exception as e:
        return error_response(e)


# Модификация количества лайков
@like.route('/modify_likes/<int:post_id>', methods=['PUT'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs({'action': fields.String()})
def modify_likes(post_id, **kwargs):
    try:
        with session.begin_nested():
            post = session.query(Post).filter(Post.post_id == post_id).first()
            if not post:
                return not_found_response('No posts with this id')
            action = kwargs['action']
            if action == 'increase':
                post.likes += 1
            elif action == 'decrease':
                post.likes = max(0, post.likes - 1)
            else:
                return error_response(f'Invalid attribute {action}')
            session.commit()
        return success_response(PostSchema(only=['likes']).dump(post))
    except Exception as e:
        return error_response(e)
