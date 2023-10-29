from django.urls import path
from catalog.views import catalog, search_books, get_books_json, search_book

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path("search/<str:query>", search_books, name='search'),
    path("get-books/", get_books_json, name='get_books_json'),
    path("search-book/", search_book, name='search_book')
]