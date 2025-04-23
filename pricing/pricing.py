import boto3

client = boto3.client('pricing')
paginator = client.get_paginator('describe_services')

""" for page in paginator.paginate():
    for service in page['Services']:
        print(service['ServiceCode\n']) """

response = paginator.paginate(
    ServiceCode = 'AmazonEC2'
)

for page in response: 
    print(page['Services'])
