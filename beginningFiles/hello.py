from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<html>"
            "<h1>Tried adding another line</h1>"
            "<p>Hello, World!</p>"
            "<h2>And another line, but with the debugger</h2>"
            "</html>")


# @app.route('/index')
# def index():
#     return 'Index Page'

@app.route('/index/')
def index():
    return 'Fuckin errored'

@app.route('/random')
def hello():
    return "I'm not real"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


