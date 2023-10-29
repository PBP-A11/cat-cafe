from django.urls import path
from mybooks.views import mybooks, get_mybooks_json, book_return

app_name = 'mybooks'

urlpatterns = [
    path('', mybooks, name='mybooks'),
    path('get-mybooks/', get_mybooks_json, name='get_mybooks_json'),
    path('book-return/<int:id>', book_return, name='book_return'),
]