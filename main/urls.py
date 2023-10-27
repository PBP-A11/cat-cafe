from django.urls import path
from main.views import main, profile_user, register

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('profile-user/', profile_user, name='profile_user'),
    path('register/', register, name='register'),
]