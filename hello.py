from flask import Flask

app = Flask(__name__)

@app.route("/")
def hnin():
    return "Hello World"

@app.route("/hnin")
def tiide():
    return "Welcome to Hnin Poe Au Kyaw"
