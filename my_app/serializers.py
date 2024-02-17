from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


