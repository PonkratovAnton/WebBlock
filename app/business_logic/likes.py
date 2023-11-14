from app.database import session
from app.models import Post
from app.schemas import PostSchema, success_response, not_found_response, error_response


def get_post_likes(post_id):
    try:
        with session.begin_nested():
            like = PostSchema().dump(session.query(Post.likes).filter(Post.post_id == post_id).first())
            if not like:
                return not_found_response('No posts with this id')
        return success_response(like)
    except Exception as e:
        return error_response(e)


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
