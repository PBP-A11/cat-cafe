from django.urls import path
from review.views import review, get_book_reviews_json, add_book_reviews_ajax

app_name = 'review'

urlpatterns = [
    path('<int:book_id>', review, name='review'),
    path('get_book_reviews_json/<int:book_id>/', get_book_reviews_json, name='get_book_reviews_json'),
    path('add_book_reviews_ajax/<int:book_id>/', add_book_reviews_ajax, name='add_book_reviews_ajax'),
]