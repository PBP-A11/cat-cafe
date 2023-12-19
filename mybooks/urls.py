from django.urls import path
from mybooks.views import mybooks, get_mybooks_json, book_return, promote_to_admin, get_mybooks_json_flutter

app_name = 'mybooks'

urlpatterns = [
    path('', mybooks, name='mybooks'),
    path('get-mybooks/', get_mybooks_json, name='get_mybooks_json'),
    path('get-mybooks-flutter/<str:username>', get_mybooks_json_flutter, name='get_mybooks_json_flutter'),
    path('book-return/<int:id>', book_return, name='book_return'),
    path('promote-to-admin/<int:id>', promote_to_admin, name='promote_to_admin'),
]