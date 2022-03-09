import boto3
from config import config

client = boto3.client('ec2',
aws_access_key_id=config["access_key"],
    aws_secret_access_key=config["secret_access_key"],
    region_name=config["region"]
)

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'BestCloud4Me'
            ]
        }
    ]
)

#for instance in response["Reservations"][0]["Instances"]:              #list
#    print(instance["InstanceId"])

#InstanceIds = []
#for instance in response["Reservations"][0]["Instances"]:              #start
#    InstanceIds.append(instance["InstanceId"])
#
#response = client.start_instances(
#    InstanceIds=InstanceIds
#)

InstanceIds = []
for instance in response["Reservations"][0]["Instances"]:
    InstanceIds.append(instance["InstanceId"])

response = client.stop_instances(
    InstanceIds=InstanceIds
)