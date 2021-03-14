#from app import app
from threading import Thread
import queue
import time
from app import settings
#import importlib
import os

# Testa att importera picamera-modulen, om vi är på pajjen
try:
    from picamera import PiCamera 
    pi_camera_exists = True
except ModuleNotFoundError:
    print('PiCamera lib didn´t exist')
    pi_camera_exists = False


class Camera_TL:
    """ Class to handle phototrig and background thread for Time Lapse"""
    def __init__(self, q, num_of_pics, num_of_pause_seconds):
        self.q = q
        self.num_of_runs = num_of_pics
        self.num_of_pause_seconds = num_of_pause_seconds
        self.actual_pic_number = 1
        if pi_camera_exists:
            self.camera = PiCamera()
            self.camera.rotation = 0

        for i in range(self.num_of_runs):
            while not self.q.empty():
                cmd = self.q.get()
                # print(f'Command is: {cmd}')
            if cmd == 'stop':
                self._stop_thread()
                return

            # print(f'Run lap no {i + 1}')
            self._trig_photo()
            time.sleep(self.num_of_pause_seconds)

        self._stop_thread()
        return

    def _stop_thread(self):
        self.q.task_done()
        settings.run_state = None
        self.actual_pic_number = 1 # Reset picture number to another round


    def _trig_photo(self):
        debug = False
        small_debug = True
        if debug: # If I want to save a text file to correct folder
            print(f"Trig photo, Pic no {self.actual_pic_number} ")
            with open(settings.pic_folder + str('Pic{:04d}').format(self.actual_pic_number) + '.txt', 'w') as outfile:
                outfile.write(f"Dummytext from Pic {self.actual_pic_number}\n\n")
        elif small_debug: # Only print the number of the pic
            print(f"Trig photo, Pic no {self.actual_pic_number} ")
        else:
            # TODO Fix photo triggering for Pi
            if pi_camera_exists:
                print(f'Fotar bild nummer {self.actual_pic_number}')
                self.camera.capture(settings.pic_folder + 'Pic{:04d}'.format(self.actual_pic_number) + '.jpg')
            else:
                print("Couldn't take a picture, module PiCamera has not been imported!")

        self.actual_pic_number += 1

class Camera_LV:
    """ Class to handle phototrig and background thread for live video """

    pic_lista = ['2021-03-10-202618_1.jpg', '2021-03-10-202538_2.jpg', '2021-03-10-202618_2.jpg', '2021-03-10-202557_4.jpg',
     '2021-03-10-202618_3.jpg', '2021-03-10-202538_4.jpg', '2021-03-10-202521.jpg', '2021-03-10-202557_3.jpg',
     '2021-03-10-202618_4.jpg', '2021-03-10-202557_2.jpg', '2021-03-10-202538_1.jpg', '2021-03-10-202557_1.jpg',
     '2021-03-10-202538_3.jpg']

    def __init__(self, q, dummy_var):
        self.q = q
        print(dummy_var)
        if pi_camera_exists:
            self.camera = PiCamera()
            self.camera.rotation = 0

        os.mkdir('app/Pictures/LiveVideo')
        self.live_pic_name = 'live_video_pic.png'


        while settings.run_state == 'live_video':
            while not self.q.empty():
                cmd = self.q.get()
                # print(f'Command is: {cmd}')
            if cmd == 'stop':
                self._stop_thread()
                return

            # print(f'Run lap no {i + 1}')
            self._trig_photo()
            time.sleep(1)

        self._stop_thread()
        return

    def _stop_thread(self):
        if os.path.isdir('app/Pictures/LiveVideo'):
            if os.path.isfile(f'app/Pictures/LiveVideo/{self.live_pic_name}'):
                os.remove(f'app/Pictures/LiveVideo/{self.live_pic_name}')
            os.rmdir('app/Pictures/LiveVideo')
        self.q.task_done()
        settings.run_state = None

    def _trig_photo(self):

        print('Fotar en bild med live video')
        with open(f'app/Pictures/LiveVideo/{self.live_pic_name}', 'w') as file:
            file.write('Test\n')


class Program1:
    """ Class for program 1"""

    def __init__(self ):
        print('Init program 1')
        self.the_thread = ...
        self.q = queue.Queue()

    def start_button_pressed(self):
        print(f'run_state from Program 1: {settings.run_state}')
        settings.run_state = 'Program1'
        print(f'run_state from Program 1: {settings.run_state}')

        # För att lägga något i kör-kön. Annars kraschar det.
        self.q.put("dummy_cmd")

        num_of_pics = settings.num_of_pics
        num_of_pause_seconds = settings.num_of_pause_seconds
        print(f'Number of pics: {num_of_pics}')
        print(f'Number of paus seconds: {num_of_pause_seconds}')

        self.the_thread = Thread(target = Camera_TL, args=(self.q, num_of_pics, num_of_pause_seconds))
        self.the_thread.setDaemon(True)
        self.the_thread.start()


    def stop_button_pressed(self):
        self.q.put('stop')


class Program2:

    """ Class för Program 2 """

    # TODO Det här programmet måste fixas om det ska vara kvar.
    
    def __init__(self):
        print('Init program 2')

    @staticmethod
    def start_button_pressed () :
        print('Inside of startbutton: Set runstate to run')
        # session['instance_running'] = 'Program2' 

    @staticmethod
    def stop_button_pressed () :
        print('Inside of stopbutton: Set runstate to none')
        # session['instance_running'] = ''

class LiveVideo:

    """ Class to handle the live video to be able to set focus and see actual camera output """
    """ Class for program 1"""

    def __init__(self):
        print('Init live video')
        self.the_thread = ...
        self.q = queue.Queue()

    def start(self):
        print(f'run_state from LiveVideo: {settings.run_state}')
        settings.run_state = 'live_video'
        print(f'run_state from LiveVideo: {settings.run_state}')

        # Just to put something in the queue, or else it crashes
        self.q.put("dummy_cmd")

        self.the_thread = Thread(target = Camera_LV, args=(self.q, 'prutt'))
        #self.the_thread = Thread(target = Camera_LV.run)
        self.the_thread.setDaemon(True)
        self.the_thread.start()
        #self.the_thread.run()


