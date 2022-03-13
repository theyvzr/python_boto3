from flask import Flask, request, jsonify
import boto3
from configparser import ConfigParser
import os
import logging


app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser()
config.read(f'{dir_path}/config.cfg')
logging.basicConfig(filename=config['LOGGING']['log_file'], level=config['LOGGING']['log_level'])

@app.route("/ec2/list", methods=["GET", "PATCH"])
def function_list():

    access_key = request.args.get("access_key")
    secret_access_key = request.args.get("secret_access_key")
    region = request.args.get("region")

    client = boto3.client('ec2',
        aws_access_key_id=f"{access_key}",
        aws_secret_access_key=f"{secret_access_key}",
        region_name=f"{region}"
    )

    response = client.describe_instances()

    if request.method == "GET":
        InstanceIds = []
        for instance in range(len(response["Reservations"])):
            InstanceIds.append(response["Reservations"][instance]["Instances"][0]["InstanceId"])
        return jsonify(InstanceIds=InstanceIds)
    elif request.method == "PATCH":
        return jsonify(response["Reservations"][0]["Instances"][0]["Placement"])


@app.route("/ec2/start", methods=["POST"])
def function_start():

    access_key = request.args.get("access_key")
    secret_access_key = request.args.get("secret_access_key")
    region = request.args.get("region")
    InstanceId = request.args.get("instanceid")

    client = boto3.client('ec2',
        aws_access_key_id=f"{access_key}",
        aws_secret_access_key=f"{secret_access_key}",
        region_name=f"{region}"
        )

    if request.method == "POST":
        response = client.start_instances(InstanceIds=[InstanceId])
        response_start = client.describe_instances()
        return jsonify(response_start["Reservations"][0]["Instances"][0]["Tags"][0])

@app.route("/ec2/stop", methods=["COPY"])
def function_stop():

    access_key = request.args.get("access_key")
    secret_access_key = request.args.get("secret_access_key")
    region = request.args.get("region")
    InstanceId = request.args.get("instanceid")

    client = boto3.client('ec2',
        aws_access_key_id=f"{access_key}",
        aws_secret_access_key=f"{secret_access_key}",
        region_name=f"{region}"
        )

    if request.method == "COPY":    
        response = client.stop_instances(InstanceIds=[InstanceId])
        response_stop = client.describe_instances()
        return jsonify(OwnerId=response_stop["Reservations"][0]["OwnerId"])

if __name__ == "__main__":
    app.run(host=config['APISERVER']['api_host'], port=config['APISERVER']['api_port'], debug=True)