import boto3

#checking the users 

iam_client = boto3.client('iam')
result = iam_client.list_users()
print(result)

print("********************************************************")

""" iam_client.create_user(
    UserName = "second_user"
)
print("done") """

iam_client.create_access_key(
    UserName = result['Users'][0]['UserName']
)

print("done")