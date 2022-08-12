from rest_framework.serializers import ModelSerializer
from .models import Book


from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
