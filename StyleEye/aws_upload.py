import boto 
from boto.s3.key import Key
bucket = aws_connection.get_bucket('mybucket')
k = Key(bucket)
k.key = 'myfile'
k.set_contents_from_filename(r'C:\Users\sadiq\Desktop\StyleEye\output.csv')