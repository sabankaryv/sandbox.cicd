import boto3
from django.conf import settings

def get_s3_client():
    return boto3.client(
        "s3",
        region_name=settings.AWS_REGION
    )

def check_s3_object_exists(s3_key):
    s3_client = get_s3_client()

    try:
        s3_client.head_object(
            Bucket=settings.AWS_S3_BUCKET_NAME,
            Key=s3_key
        )
        return True

    except s3_client.exceptions.ClientError:
        return False

def generate_download_url(s3_key):
    s3_client = get_s3_client()

    return s3_client.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": settings.AWS_S3_BUCKET_NAME,
            "Key": s3_key,
        },
        ExpiresIn=900,
    )