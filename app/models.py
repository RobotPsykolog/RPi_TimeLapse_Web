from app import app
from flask import session
from threading import Thread, Lock
import queue
import time
#from sys import exit

class lapcounter:

    def __init__(self, q):
        self.q = q
        self.lap = 0

        self.running = True

        while self.running:
            while not self.q.empty():
                cmd = self.q.get()
                print(f'Command is: {cmd}')
            if cmd == 'stop':
                self.q.task_done()
                self.running = False

            print(f'Kör varv nummer {self.lap}')
            time.sleep(1)
            self.lap += 1
        print('Avslutar trådkörning')
        return

class Programs():
    """ Föräldraklass för att kunna ärva saker """

    def __init__(self):
        pass

    @staticmethod
    def take_photo():
        print('Tar en bild med kameran')

class Program1(Programs):
    """ Klass för program 1"""

    def __init__(self):
        print('Initierar program 1')
        self.the_thread = None
        self.q = queue.Queue()

    def start_button_pressed(self):
        session['instance_running'] = 'Program1'
        self.q.put("snorkel1")
        self.q.put("snorkel2")
        self.q.put("snorkel3")
        self.q.put("snorkel4")

        self.the_thread = Thread(target = lapcounter, args=(self.q, ))
        self.the_thread.setDaemon(True)
        self.the_thread.start()


    def stop_button_pressed(self):
        self.q.put('stop')
        session['instance_running'] = ''
        print('Stoppat tråden!')


class Program2:

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

