import boto3

# connect to s3
s3 = boto3.client("s3")

# create a bucket on s3
bucket_name = s3.create_bucket(Bucket = "tech230-james-boto", CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})

print(bucket_name)