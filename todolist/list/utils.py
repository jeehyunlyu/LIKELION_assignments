from .models import ToDo, Comment
from django.contrib.auth.models import User
from todolist.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime

def upload_and_save(request, file_to_upload):
    # create client
    session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME,
    )
    s3 = session.resource('s3')

    # file upload
    now = datetime.now().strftime("%Y%H%M%S")
    user_pk = str(request.user.pk) + '/'

    try:
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + user_pk + file_to_upload.name,
            Body = file_to_upload
        )

        s3_url = 'https://todolist-jeehyunlyu.s3.ap-northeast-2.amazonaws.com/'
        todo = ToDo.objects.create(
            title = request.POST['title'],
            img = s3_url + now + user_pk + file_to_upload.name
        )
        todo.save()
        return s3_url
    
    except:
        print('첨부파일 없음')