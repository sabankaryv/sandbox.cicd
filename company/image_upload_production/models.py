from django.db import models
class Image(models.Model):
    file_name = models.CharField(max_length=255)
    s3_key = models.CharField(max_length=500,unique=True)
    content_type = models.CharField(max_length=100)
    file_size = models.PositiveBigIntegerField()
    status = models.CharField(max_length=20,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file_name