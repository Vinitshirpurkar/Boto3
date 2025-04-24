import boto3

client = boto3.client('s3')
name = "random-buck-name-new-1014"
total_buckets = client.list_buckets()
all_bucket = []
for bucket in total_buckets['Buckets']:
    all_bucket.append(bucket['Name'])
if  name not in all_bucket:
    print("Bucket does not exist, Creating now ....")
    result = client.create_bucket(
        Bucket = name
    )
    print(f"{name} is created successfully!!!") 
else:
    print("Bucket already exists")

res = client.upload_file('Samplefile.txt', name, "S3_file")
print("File uploaded successfully")

client.delete_object(
    Bucket = name,
    Key = "S3_file"
)

print("Objects deleted")

client.delete_bucket(
    Bucket = name
)

print("Bucket Deleted")




