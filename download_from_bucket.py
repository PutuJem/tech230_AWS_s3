import boto3

# connection to client
s3 = boto3.client("s3")

s3.download_file("tech230-james-boto", "sampletext.txt", "sampletext1.txt")

print(s3.download_file)