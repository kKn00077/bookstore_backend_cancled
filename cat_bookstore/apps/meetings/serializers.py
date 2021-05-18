from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        meeting = Meeting(**validated_data)
        meeting.save()
        return meeting
        
    class Meta:
            model = Meeting
            fields = '__all__'