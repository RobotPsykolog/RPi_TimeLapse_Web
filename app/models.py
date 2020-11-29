#from app import app
from threading import Thread
import queue
import time
from app import settings

#from sys import exit


class Camera:
    """ Klass för att hantera fotning och bakomliggande tråd """
    def __init__(self, q, num_of_pics, wait_seconds):
        self.q = q
        self.num_of_runs = num_of_pics
        self.wait_seconds = wait_seconds
        self.actual_pic_number = 1

        for i in range(self.num_of_runs):
            print(self.q)
            while not self.q.empty():
                cmd = self.q.get()
                print(f'Command is: {cmd}')
            if cmd == 'stop':
                self._stop_thread()
                return

            # print(f'Kör varv nummer {i + 1}')
            self._trig_photo()
            time.sleep(self.wait_seconds)

        print('Avslutar trådkörning')
        self._stop_thread()
        return

    def _stop_thread(self):
        self.q.task_done()
        settings.run_state = None


    def _trig_photo(self):
        debug = False
        small_debug = True
        if debug:
            print(f"Fotar en fot! Bild nummer {self.actual_pic_number} ")
            with open(settings.pic_folder + str('Bild{:04d}').format(self.actual_pic_number) + '.txt', 'w') as outfile:
                outfile.write(f"Hejsan från Bild{self.actual_pic_number}\n\n")
        elif small_debug:
            print(f"Fotar en fot! Bild nummer {self.actual_pic_number} ")
        else:
            # TODO Fixa fotning för pajjen
            pass
        self.actual_pic_number += 1


class Program1:
    """ Klass för program 1"""

    def __init__(self ):
        print('Initierar program 1')
        self.the_thread = None
        self.q = queue.Queue()

    def start_button_pressed(self):
        print(f'run_state från Program 1: {settings.run_state}')
        settings.run_state = 'Program1'
        print(f'run_state från Program 1: {settings.run_state}')

        # För att lägga något i kör-kön. Annars kraschar det.
        self.q.put("dummy_cmd")

        num_of_runs = 10
        wait_seconds = 0.05
        self.the_thread = Thread(target = Camera, args=(self.q, num_of_runs, wait_seconds))
        # self.q.put(self.the_thread)
        self.the_thread.setDaemon(True)
        self.the_thread.start()


    def stop_button_pressed(self):
        self.q.put('stop')


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

