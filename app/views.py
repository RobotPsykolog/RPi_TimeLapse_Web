from app import app

from app.webvideo import *
from flask import render_template, session, request
from app.models import Program1, Program2
import app.settings as settings

# Some global variables and class instances
program_1 = Program1()
program_2 = Program2()

@app.before_first_request
def before_first_request():
    settings.init()

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/livevideo')
def video():

    LiveVideo.video()
    
    return render_template('video.html')

@app.route('/program<int:number>', methods=['GET', 'POST'])
def program(number):

    if request.method == 'POST':

        if number == 1:

            if request.form['button'] == "start":
                if settings.run_state == None:
                    print('I run up to data collection')
                    settings.num_of_pics = int(request.form['num_of_pics'])
                    settings.num_of_pause_seconds = int(request.form['num_of_pause_seconds'])
                    program_1.start_button_pressed()
            else:
                if settings.run_state == 'Program1':
                    program_1.stop_button_pressed()


        else:

            if request.form['button'] == "start":
                print(f'Button start got pushed from program{number}!')
                if settings.run_state == None:
                    program_2.start_button_pressed()

            else:
                print(f'Button stop got pushed from program Knappen stopp trycktes från program {number}!')
                if settings.run_state == 'Program2':
                    program_2.stop_button_pressed()

    return render_template(f'program{number}.html', num = number)


"""
# För att cachen ska laddas om utan shift
@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response
"""