from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi "+ name

@app.route('/repeat/<num>/<text>')
def repeat(num, text):
    print (num)
    print (text)
    return (text + " ") * int(num)

app.run(debug=True)