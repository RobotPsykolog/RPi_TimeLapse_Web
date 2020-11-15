from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/program<number>')
def program(number):
    return render_template(f'program{number}.html', num = number)


# För att cachen ska laddas om utan shift
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response