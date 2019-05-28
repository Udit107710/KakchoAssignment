from django.db import models
from django.conf import settings

class UploadFileModel(models.Model):
    file = models.FileField(upload_to="uploads/original")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class FirstTaskModel(models.Model):
    file = models.FileField(upload_to="uploads/first")
    uploadfile = models.ForeignKey(UploadFileModel, on_delete= models.CASCADE)

class SecondTaskModel(models.Model):
    file = models.FileField(upload_to="uploads/second")
    firsttask = models.ForeignKey(FirstTaskModel, on_delete= models.CASCADE)

class RoundOffModel(models.Model):
    file = models.FileField(upload_to="uploads/roundoff")
    uploadfile = models.ForeignKey(UploadFileModel, on_delete= models.CASCADE)
