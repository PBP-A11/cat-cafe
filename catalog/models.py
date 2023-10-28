from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, default='N/A')
    author = models.CharField(max_length=255, default='N/A')
    preview_link = models.URLField(default='N/A')
    description = models.TextField(default='N/A')
    category = models.CharField(max_length=10, default='N/A')
    rating = models.CharField(max_length=10, default='N/A')
    is_borrowed = models.BooleanField(default=False)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_published = models.CharField(max_length=20)
    image_link = models.URLField(default='N/A')
<<<<<<< HEAD
    reviews = models.TextField(default='N/A')
=======
>>>>>>> c5c40991717f0d88f5b75616fd44c3e362b4c6ca
