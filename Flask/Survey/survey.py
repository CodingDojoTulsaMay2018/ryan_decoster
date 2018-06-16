from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def survey():
    return render_template("survey.html")

@app.route('/result')
def results():

    return render_template("result.html", name = session['name'], location = session['location'], language = session['language'])

@app.route('/danger', methods=['post'])
def danger():
    print("a user tried to visit /danger")
    session['name'] = request.form['name']
    session['location'] = request.form['location'] 
    session['language'] = request.form['language'] 

    return redirect('/result')

app.run(debug=True)