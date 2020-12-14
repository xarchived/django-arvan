import secrets

import boto3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from getter import get_setting

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
    file_name = secrets.token_urlsafe(24)  # 32 characters

    return JsonResponse(s3_client.generate_presigned_post(
        bucket_name,
        file_name,
        Fields={'acl': 'public-read'},
        Conditions=[{'acl': 'public-read'}],
        ExpiresIn=600))
