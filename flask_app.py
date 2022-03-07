from flask import Flask
import boto3


app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
