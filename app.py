# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect

import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/result', methods=['GET', 'POST'])
def birthstone():
    if request.method == 'GET':
        return "You need to post a month using the radiobuttons!"
    else:
      choice = dict(request.form)
      # Check if need dict
      month = choice['month']
      
      # Demo that request.form defaults to an ImmutableMultiDict datatype.
      print(request.form)
      
      # userdata = formopener.dict_from(request.form) # Use the Upperline-built model to convert it to a dictionary with ASCII string values.
        #print(userdata) # Show the more familiar content.

      return render_template('results.html', month="August", source="static/images/micropig.jpg", birthstone="Peridote")
