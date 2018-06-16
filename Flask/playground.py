from flask import Flask, render_template
app = Flask(__name__)

print (__name__)
@app.route('/')
def index():
    return "Welcome to the Playground!"

@app.route('/play')
def play():
    return render_template("playground.html")

@app.route('/play/<num>')
def playTimes(num):
    print(num)
    return render_template("playground.html", times = int(num))

@app.route('/play/<num>/<color>')
def playColor(num, color):
    print(num)
    print(color)
    return render_template("playground.html", times = int(num), color = "style=background-color:"+ (color))
app.run(debug=True)