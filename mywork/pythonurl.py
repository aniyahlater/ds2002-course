#!/c/Users/aniya/AppData/Local/Microsoft/WindowsApps/python3

import boto3
s3=boto3.client('s3')

#creating the function to save a file from the interent using requests
# i am lowkey not sure how I would incorporate this but I just wanted to make sure it didnt require the user to manually download the image
import urllib.request

def url(url, imageName):
	urllib.request.urlretrieve(url,imageName)

url('https://i.kinja-img.com/image/upload/c_fill,h_675,pg_1,q_80,w_1200/7298946f2a94eecc85eebf257a8877c7.jpg', 'legendOfZelda.jpg')

#vars needed
bucket_name = 'ds2002-ybf3jw'
object_name = 'legendOfZelda.jpg'
expires_in = 604800


def presignedurl(bucket_name, object_name, expires_in=604800):
	response=s3.generate_presigned_url(
	'get_object',
	Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expires_in
	)
	return response

print(presignedurl(bucket_name,'legendOfZelda.jpg',expires_in))

https://ds2002-ybf3jw.s3.amazonaws.com/legendOfZelda.jpg?AWSAccessKeyId=ASIA2UC3DLAF4UQ5VCBY&Signature=KC77yWjElAPlcbW97chDUP4SGF0%3D&x-amz-security-token=FwoGZXIvYXdzEBsaDKVzpOr4v3EBaoeQsyLEAazyj%2FZxztmBCqt5ycRHgDF%2FzUXonJgConTs%2F62rqz0iv0PhvThcbILARgH9tcyPhVxXUw4WDABlk0ITuMLNuK9Xf6t3Eig40suh9m5fDuYYeLhfz3vIZe7upAgfdjMmGLTwkIPAsIGevY9XO3SSw8UWIJgMs1gUufE2YKUqlaaDosviocT2llJwo5EDklN74dEDWA8bBOPNQFb9qQObpifhEVJe6YHw8HzDMqRUfoFyUeFyZp7NxZJOc37dCoKeIRcntooovaHurwYyLegkBJHtmSsHGVfzwUSP%2BYGbP6wlrP83fua23UG%2FBabnQ8WCKugolHg%2Bedb8Lg%3D%3D&Expires=1711591207





