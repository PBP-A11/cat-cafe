from django.urls import path
from catalog.views import catalog, search_books, get_books

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path("search/<str:query>", search_books, name='search'),
    path("get_books/", get_books, name='get_books'),
]