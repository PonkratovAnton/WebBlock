from datetime import datetime

import requests
from flask import render_template, request
from flask_apispec import use_kwargs, marshal_with

from app import post
from app.database import session
from app.models import Post, Author, Theme
from app.schemas import PostSchema, ResponseSchema, success_response, error_response, not_found_response, AuthorSchema, \
    ThemeSchema


# Отображение постов
@post.route('/posts', methods=['GET'])
@marshal_with(ResponseSchema())
def get_posts():
    try:
        with session.begin_nested():
            posts = PostSchema(many=True).dump(session.query(Post).all())
        return success_response(posts)
    except Exception as e:
        return error_response(e)


# Создание поста
@post.route('/create_post', methods=['POST'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs(PostSchema(only=['theme_id', 'content', 'author_id']), apply=True)
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


# Изменение поста
@post.route('/update_post/<int:post_id>', methods=['PUT'])
@marshal_with(ResponseSchema(exclude=['data']))
@use_kwargs(PostSchema(only=['theme_id', 'content', 'author_id']), apply=True)
def update_post(post_id, **kwargs):
    try:
        print(kwargs)
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


# Удаления поста
@post.route('/delete_post/<int:post_id>', methods=['DELETE'])
@marshal_with(ResponseSchema(exclude=['data']))
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


@post.route('/')
def display_posts():
    try:
        # Здесь нужно заменить URL на ваш реальный URL API
        api_url = 'http://127.0.0.1:5000/posts'
        response = requests.get(api_url)
        data = response.json()['data']
        return render_template('posts.html', posts=data)
    except Exception as e:
        return f"Error: {e}"


@post.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    with session.begin_nested():
        post = PostSchema().dump(session.query(Post).filter(Post.post_id == post_id).first())
        authors = AuthorSchema(many=True).dump(session.query(Author).all())
        themes = ThemeSchema(many=True).dump(session.query(Theme).all())
    return render_template('edit_post.html', post=post, authors=authors, themes=themes)


@post.route('/add_post')
def add_post():
    with session.begin_nested():
        authors = AuthorSchema(many=True).dump(session.query(Author).all())
        themes = ThemeSchema(many=True).dump(session.query(Theme).all())
    return render_template('add_post.html', authors=authors, themes=themes)
