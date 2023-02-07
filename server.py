from flask import Flask
from main import *

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/encrypt")
def func1():
    return encrypt()

@app.route("/decrypt")
def func2():
    return decrypt()

if __name__ == "__main__":
    app.run(debug=True)


