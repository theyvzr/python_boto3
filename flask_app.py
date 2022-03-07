from flask import Flask, request, jsonify, make_response
from config import config
import logging

app = Flask(__name__)

logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)

#@app.route("/hello/<name>", methods=["GET", "POST"])
#def hello_world_url_param(name):
#    surname = request.args.get("surname")
#    if surname == None:
#        surname = "Soyad Girilmedi!!!"
#    if request.method == "GET":
#        return "Hello World"
#    elif request.method == "POST":
#        return f"ad: {name}, soyad: {surname}!"

@app.route("/hello/<name>", methods=["GET", "POST"])
def hello_world_url_param(name):
    surname = request.args.get("surname")
    if surname == None:
        surname = "Soyad Girilmedi!!!"
        #logging.info("dfjnsdfkfnekfsfvk") loga root mesaj gönderir
    if request.method == "GET":
        return "Hello World"
    elif request.method == "POST":
        return make_response(jsonify(FirstName=name, LastName=surname), 500)

@app.route("/json", methods=["POST"])
def parse_json():
    json_data = request.get_json()
    print(json_data["key"])
    print(type(json_data))
    return ""

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)