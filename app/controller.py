from flask import Flask
from app import View


class Controller:
    def __init__(self):
        print('Initierar min Controller')
        self.app = Flask(__name__)
    
    def run(self):
        self.app.run()