from marshmallow import Schema, fields

from app.models import Post, Theme, Author


class AuthorSchema(Schema):
    class Meta:
        model = Author
    author_id = fields.Int(dump_only=True)
    name = fields.Str()


class ThemeSchema(Schema):
    class Meta:
        model = Theme

    theme_id = fields.Int(dump_only=True)
    name = fields.Str()


class PostSchema(Schema):
    class Meta:
        model = Post
    post_id = fields.Int(dump_only=True)
    theme_id = fields.Int()
    content = fields.Str()
    likes = fields.Int()
    author_id = fields.Int()
    pub_date = fields.DateTime(dump_only=True)
    author = fields.Pluck(AuthorSchema(), 'name')
    theme = fields.Pluck(ThemeSchema(), 'name')


class ResponseSchema(Schema):
    class Meta:
        fields = ('data', 'status', 'error')

    status = fields.String()
    error = fields.String()


def success_response(data):
    return {'data': data, 'status': 'Success', 'error': None}


def not_found_response(error_message):
    return {'data': None, 'status': 'Not Found', 'error': error_message}


def error_response(error_message):
    return {'data': None, 'status': 'Internal Server Error', 'error': error_message}
