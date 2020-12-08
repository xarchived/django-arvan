import secrets

import boto3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from getter import get_setting

access_key = '160a8999-6a17-4834-b112-3d617f7716d8'
secret_key = 'd58e63a15ca0c4f6e294c1f9ea8f2bd353553b9c723f592d21103a224407bf3a'
endpoint = 'https://s3.ir-thr-at1.arvanstorage.com'
session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id=get_setting('ARVAN', 'ACCESS_KEY'),
    aws_secret_access_key=get_setting('ARVAN', 'SECRET_KEY'),
    endpoint_url=get_setting('ARVAN', 'ENDPOINT'),
)


@csrf_exempt
@require_http_methods(['GET'])
def generate_request(request):
    bucket_name = get_setting('ARVAN', 'BUCKET_NAME')
    file_name = secrets.token_urlsafe(64)

    return JsonResponse(s3_client.generate_presigned_post(bucket_name, file_name))
