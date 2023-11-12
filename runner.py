from flask import Flask

from app import post, like

app = Flask(__name__)

app.register_blueprint(post)
app.register_blueprint(like)

if __name__ == '__main__':
    app.run(debug=False, port=8080)
