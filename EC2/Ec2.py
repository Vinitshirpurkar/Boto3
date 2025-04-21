import boto3

ec2_resource = boto3.resource('ec2')
""" ec2_resource.create_instances(ImageId='ami-0e449927258d45bc4',
                               InstanceType='t2.micro',
                               MaxCount=1,
                               MinCount=1)

print("created") """

ec2_resource.create_key_pair(
    KeyName = "my_key_pair",
    KeyFormat = 'pem'
)

