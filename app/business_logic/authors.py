from app.database import session
from app.models import Author
from app.schemas import success_response, error_response, AuthorSchema, not_found_response


def get_author(author_id=None):
    try:
        with session.begin_nested():
            if author_id is not None:
                author = AuthorSchema().dump(session.query(Author).filter(Author.post_id == author_id).first())
                if not author:
                    return not_found_response('No author with this id')
                return success_response(author)
            else:
                authors = AuthorSchema(many=True).dump(session.query(Author).all())
                return success_response(authors)
    except Exception as e:
        return error_response(e)
