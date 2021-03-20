from threading import Thread
import queue
import time
from app import settings
import os
import shutil

# Testa att importera picamera-modulen, om vi är på pajjen
try:
    from picamera import PiCamera 
    pi_camera_exists = True
except ModuleNotFoundError:
    print('PiCamera lib didn´t exist')
    pi_camera_exists = False

class Camera_TimeLapse(Thread):

    """ Class to handle Time Lapse photo taking """

    def __init__(self, num_of_pics, num_of_pause_seconds):
        super(Camera_TimeLapse, self).__init__()
        self.num_of_pics = num_of_pics
        self.num_of_pause_seconds = num_of_pause_seconds
        self.actual_pic_number = 0
        if pi_camera_exists:
            self.camera = PiCamera()
            self.camera.rotation = 0

    def _trig_photo(self):
        debug = False
        small_debug = True
        self.actual_pic_number += 1

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

    def stop_thread(self):
        settings.run_state = None
        self.actual_pic_number = 0

    def run(self):

        for i in range(self.num_of_pics):
            if settings.run_state == None:
                break
            self._trig_photo()
            time.sleep(self.num_of_pause_seconds)

        self.stop_thread()
        return



class Program1:
    """ Class for program 1"""

    def __init__(self):
        print('Init program 1')
        self.the_thread = ...

    def start_button_pressed(self):
        settings.run_state = 'Program1'

        num_of_pics = settings.num_of_pics
        num_of_pause_seconds = settings.num_of_pause_seconds

        self.the_thread = Camera_TimeLapse(num_of_pics, num_of_pause_seconds)
        self.the_thread.setDaemon(True)
        self.the_thread.start()


    def stop_button_pressed(self):
        self.the_thread.stop_thread()

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


class Camera_LiveVideo(Thread):
    """ Class to handle phototrig and background thread for live video """

    def __init__(self):
        super(Camera_LiveVideo, self).__init__()
        if pi_camera_exists:
            self.camera = PiCamera()
            self.camera.rotation = 0
        self.pic_lista = [  '2021-03-10-202618_1.jpg', '2021-03-10-202538_2.jpg', '2021-03-10-202618_2.jpg', 
                            '2021-03-10-202557_4.jpg', '2021-03-10-202618_3.jpg', '2021-03-10-202538_4.jpg', 
                            '2021-03-10-202521.jpg', '2021-03-10-202557_3.jpg', '2021-03-10-202618_4.jpg', 
                            '2021-03-10-202557_2.jpg', '2021-03-10-202538_1.jpg', '2021-03-10-202557_1.jpg',
                             '2021-03-10-202538_3.jpg']
        self.pic_pointer = 0 # Dummyvar för att peka i bildlistan

        self.live_pic_name = 'live_video_pic.jpg'
        self.livevideo_path = 'app/static/pictures/livevideo'
        if not os.path.isdir(self.livevideo_path):
            os.mkdir(self.livevideo_path)

    def run(self):
        while settings.run_state == 'live_video':
            self._trig_photo()
            time.sleep(0.05)

        self._stop_thread()
        return

    def _copy_pic(self):
        shutil.copy(f'app/static/pictures/testbilder/{self.pic_lista[self.pic_pointer]}', f'{self.livevideo_path}/{self.live_pic_name}')
        self.pic_pointer += 1
        if self.pic_pointer >= len(self.pic_lista):
            self.pic_pointer = 0

    def _trig_photo(self):
        # Trigging a photo
        self._copy_pic()

    def _stop_thread(self):
        if os.path.isdir(self.livevideo_path):
            if os.path.isfile(f'{self.livevideo_path}/{self.live_pic_name}'):
                os.remove(f'{self.livevideo_path}/{self.live_pic_name}')
            os.rmdir(self.livevideo_path)
        settings.run_state = None


class LiveVideo:

    """ Class to handle the live video to be able to set focus and see actual camera output """
    """ Class for program 1"""

    def __init__(self):
        print('Init live video')
        self.the_thread = ...

    def start(self):
        settings.run_state = 'live_video'

        self.the_thread = Camera_LiveVideo()
        self.the_thread.setDaemon(True)
        self.the_thread.start()


