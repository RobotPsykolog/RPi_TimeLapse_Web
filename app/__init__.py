from flask import Flask
#from app import global_data

app = Flask(__name__)

# Sätt jättehemlig nyckel för att kunna använda session
app.secret_key = 'hemlig_nyckel'


from app import views
from app import models
from app import settings


