from django.urls import path
from main.views import main, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]