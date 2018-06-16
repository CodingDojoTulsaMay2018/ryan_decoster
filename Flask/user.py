from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def user():
    return render_template("user.html")

@app.route('/user', methods=['post'])
def create():
    print("Got Post Info")
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    return render_template("created.html")

app.run(debug=True)