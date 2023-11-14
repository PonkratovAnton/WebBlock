import requests
from flask import render_template, request

from app import template
from app.business_logic.authors import get_author
from app.business_logic.posts import get_post
from app.business_logic.themes import get_theme
from app.database import session


@template.route('/')
def display_posts():
    try:
        url_address = f'http://{request.host}'
        api_url = f'{url_address}/posts'
        response = requests.get(api_url)
        data = response.json()['data']
        return render_template('posts.html', posts=data, url_address=url_address)
    except Exception as e:
        return f"Error: {e}"


@template.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    url_address = f'http://{request.host}'
    with session.begin_nested():
        post = get_post(post_id=post_id)['data']
        authors = get_author()['data']
        themes = get_theme()['data']
    return render_template('edit_post.html', post=post, authors=authors, themes=themes, url_address=url_address)


@template.route('/add_post')
def add_post():
    url_address = f'http://{request.host}'
    with session.begin_nested():
        authors = get_author()['data']
        themes = get_theme()['data']
    return render_template('add_post.html', authors=authors, themes=themes, url_address=url_address)
