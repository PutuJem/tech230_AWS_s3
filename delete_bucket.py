import boto3

# connect to s3
s3 = boto3.resource("s3")

bucket = s3.Bucket("tech230-james-boto")
response = bucket.delete()

print(response)