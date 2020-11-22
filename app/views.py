from app import app

from flask import render_template, session, request
from app.models import Program1, Program2

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')

@app.before_first_request
def before_first_request():
    session.clear()
    session['instance_running'] = ''

@app.route('/program<int:number>', methods=['GET', 'POST'])
def program(number):
#    global program1
    if request.method == 'POST':
        print(f"Session instance_running: {session['instance_running']}")

        if number == 1:

            if request.form['button'] == "start":
                print(f'Knappen start trycktes från program {number}!')
                if session['instance_running'] == '':
                    Program1.start_button_pressed()

                    #program.run_code()

            else:
                print(f'Knappen stopp trycktes från program {number}!')
                if session['instance_running'] == 'Program1':
                    Program1.stop_button_pressed()

        else:

            if request.form['button'] == "start":
                print(f'Knappen start trycktes från program {number}!')
                if session['instance_running'] == '':
                    Program2.start_button_pressed()

            else:
                print(f'Knappen stopp trycktes från program {number}!')
                if session['instance_running'] == 'Program2':
                    Program2.stop_button_pressed()


    return render_template(f'program{number}.html', num = number )


"""
# För att cachen ska laddas om utan shift
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response
"""