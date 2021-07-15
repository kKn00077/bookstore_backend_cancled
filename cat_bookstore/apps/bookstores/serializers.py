from rest_framework import serializers
from .models import Category, Bookstore

class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
            model = Bookstore
            fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = ['category_id', 'name']