from app import app

from app.webvideo import *
from flask import render_template, session, request
from app.models import Program1, Program2, LiveVideo
import app.settings as settings

try:
    import picamera
    pi_camera_exists = True
except ModuleNotFoundError:
    print('PiCamera lib didn´t exist')
    pi_camera_exists = False

# Some global variables and class instances
program_1 = Program1()
program_2 = Program2()
live_video = LiveVideo()

@app.before_first_request
def before_first_request():
    settings.init()

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    if settings.run_state == 'live_video':
        settings.run_state = None

    return render_template('home.html')

@app.route('/livevideo')
def video():

    if pi_camera_exists :

        with picamera.PiCamera(resolution = '640x480', framerate = 24) as camera :
            pass

            # TODO Fixa kod för att fota livevideo med pajj-kameran
            """
            output = StreamingOutput()
            
            # Uncomment the next line to change your Pi's Camera rotation (in degrees)
            camera.rotation = 0  # 180
            camera.start_recording(output, format = 'mjpeg')
            try :
                address = ('', 5000)
                server = StreamingServer(address, StreamingHandler)
                server.serve_forever()
            finally :
                camera.stop_recording()
            """
    else :
        print('Picamera existerade inte. Ska försöka fejka något')
        live_video.start()

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