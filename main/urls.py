from django.urls import path
from main.views import main, profile_user, katalog, get_product_json

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('profile-user', profile_user, name='profile_user'),
    path("get-product-json", get_product_json, name='get_product_json'),
]