from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import upload_file_to_s3, generate_signed_url
from .models import ImageUpload

import uuid

import logging
logger = logging.getLogger(__name__)
class ImageUploadView(APIView):
    def post(self, request):
        image = request.FILES.get("image")
        if not image:
            return Response(
                {
                    "error": "Image not found"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # Get information from uploaded file
        uploaded_file_name = image.name #==>File Name like WIN_20260725_13_02_26_Pro.jpg
        uploaded_file_size = image.size #size like 200000KB
        content_type = image.content_type   #application/octet-stream
        # # Allowed file types
        allowed_extensions = {
            "jpg",
            "jpeg",
            "png"
        }

        file_extension = uploaded_file_name.split(".")[-1].lower()
        if file_extension not in allowed_extensions:
            return Response(
                {
                    "error": "Only JPG, JPEG and PNG files are allowed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # # Generate unique S3 key
        s3_key = f"images/{uuid.uuid4()}.{file_extension}"  #images/unique_file_name.jpg
        print(s3_key)
        try:
            # Upload actual file directly to S3
            upload_file_to_s3(
                image=image,
                s3_key=s3_key,
                content_type=content_type
            )
            # Store metadata in DB
            image_record = ImageUpload.objects.create(
                file_name=uploaded_file_name,
                s3_key=s3_key,
                content_type=content_type,
                file_size=uploaded_file_size,
            )
            # Generate signed URL
            signed_url = generate_signed_url(
                s3_key=image_record.s3_key,
                expiration=3600,
            )
            return Response(
                {
                    "id": image_record.id,
                    "file_name": image_record.file_name,
                    "s3_key": image_record.s3_key,
                    "file_size": image_record.file_size,
                    "url": signed_url
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            print("Upload error:", e)
            return Response(
                {
                    "error": "Upload failed"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )