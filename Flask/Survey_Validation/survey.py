from flask import Flask, render_template, request, redirect, session, flash
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
    for i in request.form:
        if len(request.form[i]) == 0:
            flash("Field(s) must not be left blank!", "fieldAlert")
            return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comment is not to exceed 120 characters.", "commentAlert")
        return redirect('/')

    print("a user tried to visit /danger")
    session['name'] = request.form['name']
    session['location'] = request.form['location'] 
    session['language'] = request.form['language'] 

    return redirect('/result')

app.run(debug=True)