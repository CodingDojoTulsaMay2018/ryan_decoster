from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'ThisIsSecret'

mysql = connectToMySQL('logindb')
print("all the users", mysql.query_db("SELECT * FROM users;"))


@app.route('/')
def index():
    debugHelp("INDEX METHOD")
    return render_template("index.html")

@app.route('/login', methods=['post'])
def login():
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form['email'] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']

            print(session['userid'])
            return redirect('/welcome')
    flash("Incorrect email or password!", "loginAlert")
    return redirect('/')


@app.route('/create', methods=['post'])
def create():
    for i in request.form:
        if len(request.form[i]) == 0:    
            flash("All fields are required and must not be blank!", "fieldAlert")
            return redirect('/')
    if request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("Name must contain characters only!", "nameAlert")
    elif len(request.form['first_name']) < 2:
        flash("Name must be more than two characters!", "nameAlert")
    elif len(request.form['last_name']) < 2:
        flash("Name must be more than two characters!", "nameAlert")

    if len(request.form['password']) < 8:
        flash("Password needs to be longer!", "passwordAlert")    
    elif request.form['password'] != request.form['confirm']:
        flash("Passwords do not match!", "passwordAlert")
       
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", "emailAlert")   
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "emailAlert")
        
    debugHelp('RESERVE METHOD')
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        queryEmail = "SELECT email FROM users WHERE email=%(email)s;" 
        emailData = {
            'email': request.form['email'] 
        }
        emailcheck = mysql.query_db(queryEmail,emailData)
        if (emailcheck):
            flash("Email already taken!", "emailAlert")
            return redirect('/')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])  
        print(pw_hash)
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
        data = { "first_name" : request.form['first_name'],
                 "last_name" : request.form['last_name'],
                 "email" : request.form['email'],
                 "password_hash" : pw_hash }
        mysql.query_db(query, data)
        return redirect("/welcome")

@app.route('/welcome')
def welcome():
    
    return render_template('welcome.html')

def debugHelp(message = ""):
    print("\n\n-----------------------", message, "--------------------")
    print('REQUEST.FORM:', request.form)
    print('SESSION:', session)
app.run(debug=True)




