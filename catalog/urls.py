from django.urls import path
from catalog.views import catalog, search_books, get_books_json, search_book, book_borrowed, delete_book, add_book, add_book_flutter
from user_profile.views import get_user_json

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path("search/<str:query>", search_books, name='search'),
    path("get-books/", get_books_json, name='get_books_json'),
    path("search-book/", search_book, name='search_book'),
    path("borrow-book/<int:id>", book_borrowed, name='borrow_book'),
    path("delete-book/<int:id>", delete_book, name='delete_book'),
    path('get-user/', get_user_json, name='get_user_json'),
    path('add-book/', add_book, name='add_book'),
    path('add-book-flutter/', add_book_flutter, name='add_book_flutter'),
]