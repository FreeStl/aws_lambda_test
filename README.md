1) Create buckets for uploading .jpg and downloading .png
![Screenshot 2023-10-15 142431.png](pics%2FScreenshot%202023-10-15%20142431.png)
2) Create Lambda function. I use Amazon Python "Get S3 Object" IMA. Create Role for this lambda.
Add s3 bucket event "object created" as event source
![img.png](img.png)
![img_4.png](img_4.png)
3) Add layer with Python 'Pillow' library, so we can convert picture type
![img_2.png](img_2.png)
4) Add our lambda role permission to our s3 buckets
![img_3.png](img_3.png)
5) Add code to our lambda function (in folder ./func)
7) upload a .jpg file to our input bucket. In my case it is "mnazaruk-input". PNG version of this file will appear in output bucket (mnazaruk-output)