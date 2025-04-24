import boto3

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
instance_name = "Boto3-Instance"

avail_instance_names = []

for instance in ec2.instances.all():
    tags = instance.tags or [] 
    for tag in tags:
        if tag['Key'] == 'Name':
            avail_instance_names.append(tag['Value'])


if instance_name not in avail_instance_names:
    print("Instance does not exist, creating now...")
    ec2.create_instances(
        ImageId='ami-0e449927258d45bc4',  
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
        ]
    )
else:
    print("Instance already exists.")

ec2_client.stop_instances(
    InstanceIds=[
        'i-0da4174b3556bcb3a',
    ]
)
print('stop')

ec2_client.terminate_instances(
    InstanceIds=[
        'i-0da4174b3556bcb3a',
    ]
)

print('terminate')