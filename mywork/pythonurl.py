#!/c/Users/aniya/AppData/Local/Microsoft/WindowsApps/python3

import boto3
s3=boto3.client('s3')

#vars needed
bucket_name = 'ybf3jw'
object_name = 'imagereq'
expires_in = 604800

#creating the function to save a file from the interent using requests
#import requests

#def url(urlc):
#r=requests.get(urlc,allow_redirects=True)

def presignedurl(bucket_name, object_name, expires_in=604800):
	response=s3.generate_presigned_url(
	'get_object',
	Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expires_in
	)
	return response

print(presignedurl(bucket_name,object_name,expires_in))




