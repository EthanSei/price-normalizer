from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session, flash
from arcgis.gis import GIS

#-----------------------------------------------------------------------

app = Flask(__name__)
gis = GIS()

@app.route('/', methods=['GET'])
def index():
    html = render_template('home.html', session=session)
    return make_response(html)

@app.route('/profile', methods=['GET'])
def profile():
    return "profile"
    

if __name__ == '__main__':
    app.run('localhost', port=55555, debug=True)