from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("checkerboard.html")

@app.route('/<x>/<y>')
def manyChecks(x, y):
    return render_template("checkerboard.html", first = int(int(x)/2), second = int(int(y)/2))

app.run(debug=True)