from django.urls import path
from .views import GenerateUploadURLView,ConfirmUploadView,GenerateDownloadURLView

urlpatterns=[
    path("",GenerateUploadURLView.as_view(),name="image_upload_prod"),
    path("<int:image_id>/confirm/",ConfirmUploadView.as_view(),name="confirm-upload"),
    path("<int:image_id>/download/",GenerateDownloadURLView.as_view(),name="generate-download-url")
]