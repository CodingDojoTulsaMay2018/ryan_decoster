import random
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
    session['num'] = random.randint(1,100)

@app.route('/')
def index():
    if 'num' not in session:
        setSession()
    else:
        pass
    print(session['num'])
    return render_template("index.html")

@app.route('/guess', methods=['post'])
def guessNum():
    guess = request.form['guess']
    if request.method == 'POST':
        if guess.isdigit():
            msg = ""
            numguess = int(guess)
            if numguess == session['num']:
                msg = "Correct!"
                color = 'green'
            elif numguess > session['num']:
                msg = "Too High"
                color = 'red'
            else:
                msg = "Too Low"
                color = 'red'
        else:
            msg = "Not a valid guess"
    elif isinstance(guess, str):
        msg = "Not a valid guess"
    else:
        msg = "Not a valid guess"

    print("message", msg)
    print(request.form)
    return render_template("guess.html", msg = msg, color = "style=background-color:"+ (color))


@app.route('/reset', methods=['post'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)