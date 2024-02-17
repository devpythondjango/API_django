from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, BooksViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BooksViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls