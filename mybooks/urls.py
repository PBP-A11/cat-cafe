from django.urls import path
from mybooks.views import mybooks, get_mybooks_json

app_name = 'mybooks'

urlpatterns = [
    path('', mybooks, name='mybooks'),
    path('get-mybooks/', get_mybooks_json, name='get_mybooks_json'),
]