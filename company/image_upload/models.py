from django.db import models

from django.db import models


class ImageUpload(models.Model):
    file_name = models.CharField(max_length=255)
    s3_key = models.CharField(max_length=500)
    content_type = models.CharField(max_length=100)
    file_size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file_name