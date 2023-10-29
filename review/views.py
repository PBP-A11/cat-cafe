from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
import os
from catalog.models import Book
from main.models import BookReview
from django.views.decorators.csrf import csrf_exempt

# @login_required(login_url='/login')
def review(request, book_id):
    context = {
        'book': Book.objects.get(pk = book_id),
        'id': book_id }
    return render(request, "review.html", context)

@csrf_exempt
def add_book_reviews_ajax(request, book_id):
    if request.method == 'POST' and request.user.is_authenticated:
        book = Book.objects.get(pk = book_id)
        user = request.user
        content = request.POST.get("content")
        stars = request.POST.get("stars")
        date_added = request.user

        try:
            if int(stars) < 0 or int(stars) > 5:
                return HttpResponseBadRequest("invalid stars value. please rate between 0 to 5.")
        except:
            return HttpResponseBadRequest("invalid stars value. please rate between 0 to 5.")

        new_book_review = BookReview.objects.create(book = book, user = user, content = content, stars = stars, date_added = date_added)

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_book_reviews_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    try:
        book_review = BookReview.objects.filter(book__id=book_id)
        print("miau")
    except BookReview.DoesNotExist:
        book_review = None
        print("miau1")
    
    for review in book_review:

        print(review.user)

    data = [{
        'user': review.user.username,
        'content': review.content,
        'stars': review.stars,
        'date_added': review.date_added

    } for review in book_review]
    # return HttpResponse(serializers.serialize('json', book_review))
    return JsonResponse({'book_review': data})