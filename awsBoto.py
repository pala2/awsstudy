#Script for testing aws s3 using boto3
import boto3
import botocore
import os

bucketName = 'pekka.examplebucket'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucketName)

try:
    s3.meta.client.head_bucket(Bucket=bucketName)
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
    	print "No bucket"
    	os._exit(1)

for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)
