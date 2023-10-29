from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from catalog.models import Book

class User(AbstractUser):
    ROLES = [('MEMBER', 'Member'),
             ('ADMIN', 'Admin')]
    user_type = models.CharField(max_length=20, choices=ROLES, default='MEMBER')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    fav_color = models.CharField(max_length=255)

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

class BookReview(models.Model):
    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = 'reviews', on_delete = models.CASCADE)

    content = models.TextField(blank = True, null = True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True)
