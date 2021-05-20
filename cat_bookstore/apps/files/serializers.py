from rest_framework import serializers
from .models import File, FileGroup

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'order']
        extra_kwargs = {
            'file': {"allow_empty_file":False, "use_url": True},
            'order': {"required": False, "allow_null": True},
        }