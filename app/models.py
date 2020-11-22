from app import app
from flask import session
import threading
import time
from sys import exit

class Programs(threading.Thread):
    """ Föräldraklass för att kunna ärva saker """

    def __init__(self):
        super(Programs, self).__init__()


    @staticmethod
    def take_photo():
        print('Tar en bild med kameran')

    def run(self):
        print("Kör tråd från Program1")
        lap = 1
        #while self.flag_running:
        while session['instance_running'] == 'Program1':
        #for lap in range(10):
            print(f'Kör varv nummer {lap}')
            time.sleep(1)
            lap += 1


class Program1(threading.Thread):
    """ Klass för program 1"""

    """
    def __init__(self):
        super(Program1, self).__init__()
        print('Initierar program 1')
        self.the_thread = None
        self.flag_running = False
    """
    @staticmethod
    def start_button_pressed():
        session['instance_running'] = 'Program1'
        thread = Programs()
        thread.start()


    """ 
    def start_button_pressed(self):

        print('Inne i startbutton: Sätter körstatus till kör')
        session['instance_running'] = 'Program1'
        threading.Thread(None, self).__init__()
        self.the_thread = threading.Thread()
        self.flag_running = True
        self.the_thread.start()
        print("Efter thread start")
    """
    @staticmethod
    def stop_button_pressed():
        session['instance_runnning'] = ''

    """
    def stop_button_pressed(self):
        print('Inne i stopbutton: Sätter körstatus till inget')
        session['instance_running'] = ''
        print("Stoppar tråden!")
        self.flag_running = False
    """



class Program2(Programs, threading.Thread):

    """ Klass för Program 2 """

    def __init__(self):
        print('Initierar program 2')

    @staticmethod
    def start_button_pressed () :
        print('Inne i startbutton: Sätter körstatus till kör')
        session['instance_running'] = 'Program2'

    @staticmethod
    def stop_button_pressed () :
        print('Inne i stopbutton: Sätter körstatus till inget')
        session['instance_running'] = ''

