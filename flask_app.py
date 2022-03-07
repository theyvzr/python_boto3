from flask import Flask
import boto3
from config import config

client = boto3.client()


app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
