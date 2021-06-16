from rest_framework import serializers
from apps.utils.exceptions import CommonExceptions
from apps.bookstores.models import Category
from .models import CategorySubscribe

class CategorySubscribeSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def validate(self, attrs):

        if not self.context.get('user'):
            raise CommonExceptions.NotFoundUser()

        return super().validate(attrs)

    def create(self, validated_data):
        """
            이미 사용자가 구독을 하고 있는 카테고리이면 저장을 하지 않고
            새로 구독하는 카테고리일 경우 create를 함
        """
        
        user = self.context["user"]
        queryset = CategorySubscribe.objects.filter(account=user, **validated_data)

        if not queryset.exists():
            category_subscribe = CategorySubscribe.objects.create(
                account=user, **validated_data)
        else:
            category_subscribe = queryset.get()

        return category_subscribe