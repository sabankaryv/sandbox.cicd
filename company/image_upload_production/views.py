from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .service import get_s3_client,check_s3_object_exists,generate_download_url
from django.conf import settings
import uuid
from .models import Image
class GenerateUploadURLView(APIView):
    def post(self,request):
        file_name = request.data.get("file_name")
        content_type = request.data.get("content_type")
        file_size = request.data.get("file_size")
        # -----------------------------
        # 1. Required fields
        # -----------------------------
        if not file_name:
            return Response(
                {"error": "file_name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not content_type:
            return Response(
                {"error": "content_type is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not file_size:
            return Response(
                {"error": "file_size is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # -----------------------------
        # 2. Validate file size
        # -----------------------------
        try:
            file_size = int(file_size)
        except (TypeError, ValueError):
            return Response(
                {"error": "file_size must be a valid number"},
                status=status.HTTP_400_BAD_REQUEST
            )

        MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

        if file_size <= 0:
            return Response(
                {"error": "file_size must be greater than 0"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if file_size > MAX_FILE_SIZE:
            return Response(
                {"error": "Maximum file size is 5 MB"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # -----------------------------
        # 3. Validate content type
        # -----------------------------
        allowed_types = {
            "image/jpeg",
            "image/png",
        }
        if content_type not in allowed_types:
            return Response(
                {"error": "Only JPEG and PNG images are allowed"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # -----------------------------
        # 4. Get extension
        # -----------------------------
        extension = file_name.rsplit(".", 1)[-1].lower()
         # -----------------------------
        # 6. Generate presigned URL
        # -----------------------------
        s3_client = get_s3_client()
        # -----------------------------
        # 5. Generate unique S3 key
        # -----------------------------
        s3_key = f"images/{uuid.uuid4()}.{extension}"
        upload_url = s3_client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": settings.AWS_S3_BUCKET_NAME,
                "Key": s3_key,
                "ContentType": content_type,
            },
            ExpiresIn=900,
        )
        # -----------------------------
        # 7. Save metadata
        # -----------------------------
        image = Image.objects.create(
            file_name=file_name,
            s3_key=s3_key,
            content_type=content_type,
            file_size=file_size,
            status="PENDING",
        )
        # -----------------------------
        # 8. Return response
        # -----------------------------
        return Response(
            {
                "image_id": image.id,
                "upload_url": upload_url,
                "s3_key": s3_key,
                "expires_in": 900,
            },
            status=status.HTTP_201_CREATED
        )

class ConfirmUploadView(APIView):
    def post(self, request, image_id):
        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return Response(
                {"error": "Image not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        # Check whether object exists in S3
        exists = check_s3_object_exists(image.s3_key)
        if not exists:
            return Response(
                {
                    "error": "Image does not exist in S3"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # Update status
        image.status = "UPLOADED"
        image.save(update_fields=["status", "updated_at"])
        return Response(
            {
                "image_id": image.id,
                "status": image.status,
                "s3_key": image.s3_key
            },
            status=status.HTTP_200_OK
        )
class GenerateDownloadURLView(APIView):
    def get(self, request, image_id):
        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return Response(
                {"error": "Image not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        if image.status != "UPLOADED":
            return Response(
                {"error": "Image is not uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )
        download_url = generate_download_url(image.s3_key)
        return Response(
            {
                "image_id": image.id,
                "file_name": image.file_name,
                "download_url": download_url,
                "expires_in": 900,
            },
            status=status.HTTP_200_OK
        )