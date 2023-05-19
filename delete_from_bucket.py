import boto3

# connect to s3
s3 = boto3.resource("s3")

# delete the file in a particular bucket
s3.Object("tech230-james-boto", "sampletext.txt").delete()
