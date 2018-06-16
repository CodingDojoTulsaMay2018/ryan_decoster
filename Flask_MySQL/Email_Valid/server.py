from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = connectToMySQL('emaildb')
print("all the emails", mysql.query_db("SELECT * FROM emails;"))

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email is not valid!", "emailAlert")
        return redirect('/') 
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!", "emailAlert")
        return redirect('/')
    else:
        flash("The email address you entered " + request.form['email'] + " is a VALID email address! Thank you!", "successAlert")
    
    query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
    data = {
            'email': request.form['email']
           }
    mysql.query_db(query, data)
    print(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    all_emails = mysql.query_db("SELECT * FROM emails;")
    print("Fetched all emails", all_emails)
    return render_template('success.html', emails = all_emails)

@app.route('/delete')
def delete():
    mysql.query_db("DELETE FROM emails ORDER BY id DESC limit 1;")
    print("Deleted previous addition")
    return redirect('success')

if __name__ == "__main__":
    app.run(debug=True)