from app.database import session
from app.models import Theme
from app.schemas import success_response, error_response, not_found_response, ThemeSchema


def get_theme(theme_id=None):
    try:
        with session.begin_nested():
            if theme_id is not None:
                theme = ThemeSchema().dump(session.query(Theme).filter(Theme.post_id == theme_id).first())
                if not theme:
                    return not_found_response('No theme with this id')
                return success_response(theme)
            else:
                themes = ThemeSchema(many=True).dump(session.query(Theme).all())
                return success_response(themes)
    except Exception as e:
        return error_response(e)
