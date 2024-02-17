from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title