from flask import Flask, render_template, redirect, request, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['post'])
def create():
    for i in request.form:
        if len(request.form[i]) == 0:    
            flash("All fields are required and must not be blank!", "fieldAlert")
    if request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("Name must contain characters only!", "nameAlert")
        return redirect('/')
    if len(request.form['password']) < 8:
        flash("Password needs to be longer!", "passwordAlert")
        return redirect('/')
    if request.form['password'] != request.form['confirm']:
        flash("Passwords do not match!", "passwordAlert")
        return redirect('/')  
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", "emailAlert")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "emailAlert")
    
    else:
        flash("Thanks for submitting your information!", "successAlert")
    return redirect('/')

app.run(debug=True)