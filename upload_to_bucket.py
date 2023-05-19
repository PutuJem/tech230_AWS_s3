import boto3

# connect to s3
s3 = boto3.resource("s3")

# open the file we want to send, store it in a variable called data
data = open("sampletext.txt", "rb")

# specify what bucket we are sending the file to
s3.Bucket("tech230-james-boto").put_object(Key="sampletext.txt", Body=data)
