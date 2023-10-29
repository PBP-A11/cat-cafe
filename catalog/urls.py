from django.urls import path
from catalog.views import catalog, search_books, get_books_json, get_book_reviews_json, add_book_reviews_ajax

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path("search/<str:query>", search_books, name='search'),
    path("get-books/", get_books_json, name='get_books_json'),
    path('get_book_reviews_json/<int:book_id>/', get_book_reviews_json, name='get_book_reviews_json'),
    path('add_book_reviews_ajax/<int:book_id>/', add_book_reviews_ajax, name='add_book_reviews_ajax')
]