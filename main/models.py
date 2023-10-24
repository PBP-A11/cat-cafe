from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLES = [('MEMBER', 'Member'),
             ('ADMIN', 'Admin')]
    user_type = models.CharField(max_length=20, choices=ROLES, default='MEMBER')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

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

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, blank=True)
    
    class Meta:
        permissions = [
            ("can_view_member_profile", "Can view member profile"),
            ("can_borrow_books", "Can borrow books"),
        ]

class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        permissions = [
            ("can_view_admin_profile", "Can view admin profile"),
            ("can_view_member_list", "Can view member list"),
        ]
