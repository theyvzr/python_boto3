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
            'Name': 'key-name',
            'Values': [
                'BestCloud4Me'
            ]
        }
    ]
)

print(response["Reservations"][0])

#print(response["Reservations"][0]["Instances"][0])

#for instance in response["Reservations"][0]["Instances"]:
#    print(instance["InstanceId"])

#response = client.start_instances(
#    InstancesIds=InstancesIds
#)