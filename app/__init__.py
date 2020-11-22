from flask import Flask

app = Flask(__name__)

# Sätt jättehemlig nyckel för att kunna använda session
app.secret_key = 'hemlig_nyckel'


from app import views

from app import models


