from flask import Flask

from app import post, like, template
from config import app_port, host

app = Flask(__name__)

app.register_blueprint(post)
app.register_blueprint(like)
app.register_blueprint(template)

if __name__ == '__main__':
    app.run(debug=False, host=host, port=app_port)

