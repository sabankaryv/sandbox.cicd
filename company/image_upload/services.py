import boto3
from django.conf import settings


def get_s3_client():
    return boto3.client(
        "s3",
        region_name=settings.AWS_REGION
    )
def upload_file_to_s3(image, s3_key, content_type):
    s3_client = get_s3_client()
    s3_client.upload_fileobj(
        image,
        settings.AWS_S3_BUCKET_NAME,
        s3_key,
        ExtraArgs={
            "ContentType": content_type
        }
    )
def generate_signed_url(s3_key, expiration=3600):
    s3_client = get_s3_client()
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_S3_BUCKET_NAME,
            "Key": s3_key,
        },
        ExpiresIn=expiration,
    )