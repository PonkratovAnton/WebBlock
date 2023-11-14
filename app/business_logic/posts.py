from datetime import datetime

from app.database import session
from app.models import Post
from app.schemas import PostSchema, success_response, error_response, not_found_response


def get_post(post_id=None):
    try:
        with session.begin_nested():
            if post_id is not None:
                post = PostSchema().dump(session.query(Post).filter(Post.post_id == post_id).first())
                if not post:
                    return not_found_response('No post with this id')
                return success_response(post)
            else:
                posts = PostSchema(many=True).dump(session.query(Post).all())
                return success_response(posts)
    except Exception as e:
        return error_response(e)


def create_post(**kwargs):
    try:
        data = kwargs
        with session.begin_nested():
            data['pub_date'] = datetime.now()
            post = Post(**data)
            session.add(post)
            session.commit()
        return success_response(PostSchema().dump(post))
    except Exception as e:
        return error_response(e)


def update_post(post_id, **kwargs):
    try:
        with session.begin_nested():
            item = session.query(Post).filter(Post.post_id == post_id).first()
            if not item:
                return not_found_response('No posts with this id')
            for key, value in kwargs.items():
                setattr(item, key, value)
            session.commit()
        return success_response(PostSchema().dump(item))
    except Exception as e:
        return error_response(str(e))


def delete_post(post_id):
    try:
        with session.begin_nested():
            item = session.query(Post).filter(Post.post_id == post_id).first()
            result = PostSchema().dump(item)
            if not item:
                return not_found_response('No posts with this id')
            session.delete(item)
            session.commit()
            return success_response(result)
    except Exception as e:
        return error_response(e)



