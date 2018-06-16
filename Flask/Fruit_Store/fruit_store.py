from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def store():
    return render_template("fruit_store.html")

@app.route('/checkout')
def checkout():
    print(request.form)
    return render_template("checkout.html", count = session['count'], strawberry = session['strawberry'], rasberry = session['rasberry'], apple = session['apple'], name = session['name'], id = session['id'])

@app.route('/danger', methods=['post'])
def danger():
    print('a user tried to visit danger')
    session['strawberry'] = request.form['strawberry']
    session['rasberry'] = request.form['rasberry']
    session['apple'] = request.form['apple']
    session['count'] = int(request.form['strawberry'])+int(request.form['rasberry'])+int(request.form['apple'])
    session['name'] = request.form['name']
    session['id'] = request.form['id']
    return redirect('/checkout')

app.run(debug=True)