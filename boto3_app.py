import boto3
from config import config

client = boto3.client('ec2',
    aws_access_key_id=config["access_key"],
    aws_secret_access_key=config["secret_access_key"],
    region=config["region"]
)

response = client.describe_instances(
    Fliters=[
        {
            'Name': 'key-name',
            'Values': [
                'BestCloud4Me'
            ]
        }
    ]
)

InstancesIds = []
for instance in response["Reservations"][0]["Instances"]:
    InstancesIds.append(instance["InstanceId"])

response = client.start_instances(
    InstancesIds=InstancesIds
)