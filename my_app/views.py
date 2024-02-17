from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer
from .models import Books

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
