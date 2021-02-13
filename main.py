from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session, flash

#-----------------------------------------------------------------------

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "hello world"

@app.route('/profile', methods=['GET'])
def profile():
    return "profile"

if __name__ == '__main__':
    app.run('localhost', port=55555, debug=True)