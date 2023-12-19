from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('<int:book_id>', review, name='review'),
    path('get_book_reviews_json/<int:book_id>/',
         get_book_reviews_json, name='get_book_reviews_json'),
    path('add_book_reviews_ajax/<int:book_id>/',
         add_book_reviews_ajax, name='add_book_reviews_ajax'),
    path('add_book_reviews_json/<int:book_id>/',
         add_book_reviews_json, name='add_book_reviews_json'),
    path('edit_book_reviews_json/<int:review_id>/',
         edit_book_reviews_json, name='edit_book_reviews_json'),
    path('delete_book_reviews_json/<int:review_id>/',
         delete_book_reviews_json, name='delete_book_reviews_json'),

]
