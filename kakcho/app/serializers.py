from rest_framework import serializers
from .models import UploadFileModel

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFileModel
        fields = ['__all__']
