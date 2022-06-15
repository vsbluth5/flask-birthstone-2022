# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect

from model import get_birthstone

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
      # request.form defaults to an ImmutableMultiDict datatype.
      print(request.form)
      
     # choice = dict(request.form)
      choice = request.form
      month = choice['month']
     #  bstone = {'month': 'January', 'name':'Garnet', 'source':'static/images/jan_garnet.webp'}
      bstone = get_birthstone(month)

      return render_template('results.html', birthstone = bstone)
