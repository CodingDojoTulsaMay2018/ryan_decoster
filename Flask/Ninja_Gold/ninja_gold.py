import random
import datetime

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'color' not in session:
        session['color'] = "black"
    color = session['color']
    
    return render_template("index.html", color=color)

@app.route('/process_money', methods=['post'])
def process():
    if request.form['building'] == 'farm':
        collected = random.randrange(10, 20)
        session['gold'] += collected
        color = session['color']
        session['color'] = "green"
        session['activities'].append('Earned ' + str(collected) + ' gold from the farm! (' + '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

    elif request.form['building'] == 'cave':
        collected = random.randrange(5, 10)
        session['gold'] += collected
        session['color'] = "green"
        session['activities'].append('Earned ' + str(collected) + ' gold from the cave! (' + '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

    elif request.form['building'] == 'house':
        collected = random.randrange(2, 5)
        session['gold'] += collected
        session['color'] = "green"
        session['activities'].append('Earned ' + str(collected) + ' gold from the house! (' + '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))

    elif request.form['building'] == 'casino':
        collected = random.randrange(-50, 50)
        session['gold'] += collected
        if collected > 0:
            session['color'] = "green"
            session['activities'].append('Entered the casino and won '+ str(collected) + ' gold! Nice! (' + '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
        else:
            session['color'] = "red"
            session['activities'].append('Entered the casino and lost '+ str(collected) + ' gold! Ouch! (' + '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())) 

    return redirect('/')

app.run(debug=True)