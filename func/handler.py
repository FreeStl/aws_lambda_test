import json
import urllib.parse
import boto3
from PIL import Image
from io import BytesIO

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = ""
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
        print("0")
    file_content = response['Body'].read()
    image = Image.open(BytesIO(file_content))

    imgByteArr = BytesIO()
    image.save(imgByteArr, format='PNG')

    destination_bucket_name = 'mnazaruk-output'
    new_file_key = key.split('.')[0] + '.png'
    s3.put_object(Body=imgByteArr, Bucket=destination_bucket_name, Key=new_file_key)


