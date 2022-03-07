from flask import Flask, request

app = Flask(__name__)

@app.route("/hello/<name>", methods=["Get", "POST"])
def hello_world(name):
   # name = request.args.get("key")
    if request.method == "GET":
        return "Hello World"
    elif request.method == "POST":
        return f"Hello, {name}"

@app.route("/bye")
def goodbye_world():
    return "Good bye"

app.run(debug=True)