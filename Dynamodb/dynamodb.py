import boto3
dynamodb_client = boto3.client('dynamodb')

table_name = 'University'


""" table = dynamodb_client.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'University',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'City',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'University',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'City',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
) """

dynamodb_client.put_item(
    TableName = table_name, 
    Item = {
        'University': {'S': 'ABC'},
        'City': {'S': 'CA'}, 
        'Rank': {'N': '1'},
        'Country': {'S': 'USA'}
    }

)

dynamodb_client.delete_item(
    TableName = table_name,
    Key = {
        'University': {'S': 'ABC'},
        'City': {'S': 'CA'}
    }

)

print("deleted")