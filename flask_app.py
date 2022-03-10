from flask import Flask, request, jsonify, make_response
import boto3
from config import config
import logging

app = Flask(__name__)

logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)

@app.route("/ec2/list", methods=["GET"])
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

    try:
        request.method == "GET"
        InstanceIds = []
        for instance in response["Reservations"][0]["Instances"]:
            InstanceIds.append(instance["InstanceId"])
        return jsonify(InstanceIds=InstanceIds)
    except:
        return "Wrong HTTP methods used!"

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
        return "Your instance has been started."


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
        return "Your instance has been stopped."

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)