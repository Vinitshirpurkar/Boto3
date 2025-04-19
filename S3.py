# Checking s3 buckets 
import boto3
s3_client = boto3.client('s3')

buckets = s3_client.list_buckets(BucketRegion = 'us-east-1')
print(buckets) 

#creating bucket 
#defining bucket name as obj
bucket_name = "my-bucket-95gw5i0b"

s3_client.create_bucket(Bucket = bucket_name)
print(f"Bucket is created {bucket_name}") 

#adding file into bucket 
#create file 

with open("sample_text.txt","w") as file: 
    file.write("this is the sample file")

s3_client.upload_file("sample_text.txt", bucket_name, "s3_text_file") 

key = "s3_text_file"

s3_client.delete_object(
    Bucket = bucket_name, Key = key
) 

s3_client.delete_bucket(
    Bucket = bucket_name
)



