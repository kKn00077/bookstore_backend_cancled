from rest_framework import serializers
from .models import File, FileGroup

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['path', 'order']
        extra_kwargs = {
            'path': {"allow_empty_file":False, "use_url": True},
            'order': {"required": False, "allow_null": True},
        }