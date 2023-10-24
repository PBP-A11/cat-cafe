from django.urls import path
from main.views import main, profile_user, katalog

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('profile_user', profile_user, name='profile_user'),
    path('katalog', katalog, name='katalog')
]