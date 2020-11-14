from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/program1')
def program1():
    return render_template('program1.html')

@app.route('/program2')
def program2():
    return render_template('program2.html')


# För att cachen ska laddas om utan shift
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response