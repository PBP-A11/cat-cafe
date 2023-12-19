from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
import os
from catalog.models import Book
from main.models import BookReview
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user
import json
# @login_required(login_url='/login')


def review(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id),
        'id': book_id}
    return render(request, "review.html", context)


@csrf_exempt
def add_book_reviews_ajax(request, book_id):
    if request.method == 'POST' and request.user.is_authenticated:
        book = Book.objects.get(pk=book_id)
        user = request.user
        content = request.POST.get("content")
        stars = request.POST.get("stars")
        date_added = request.user

        try:
            if int(stars) < 0 or int(stars) > 5:
                return HttpResponseBadRequest("invalid stars value. please rate between 0 to 5.")
        except:
            return HttpResponseBadRequest("invalid stars value. please rate between 0 to 5.")

        new_book_review = BookReview.objects.create(
            book=book, user=user, content=content, stars=stars, date_added=date_added)

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
def add_book_reviews_json(request, book_id):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return HttpResponseNotFound("Book not found.")

        user = get_user(request)

        data = json.loads(request.body)
        content = data['content']
        stars = data['stars']

        print(stars)

        try:
            stars = int(stars)
            if stars < 0 or stars > 5:
                return HttpResponseBadRequest("Invalid stars value. Please rate between 0 to 5.")
        except ValueError:
            return HttpResponseBadRequest("Invalid stars value. Please provide a valid integer.")

        date_added = get_user(request)

        new_book_review = BookReview.objects.create(
            book=book, user=user, content=content, stars=stars, date_added=date_added)

        response_data = {
            'status': True,
            'message': 'Review successfully added.',
        }

        return JsonResponse(response_data, status=200)

    return JsonResponse({
        'status': False,
        'message': 'Failed adding review.',
    }, status=201)


@csrf_exempt
def edit_book_reviews_json(request, review_id):
    if request.method == 'POST':
        try:
            book_review = BookReview.objects.get(pk=review_id  )
            print(book_review)
        except BookReview.DoesNotExist:
            return HttpResponseNotFound("Book not found.")

        data = json.loads(request.body)

        book_review.content = data['content']
        book_review.stars = data['stars']
        book_review.save()

        response_data = {
            'status': True,
            'message': 'Review successfully edited.',
        }

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({
            'status': False,
            'message': 'Failed editing review',
        }, status=200)


@csrf_exempt
def delete_book_reviews_json(request, review_id):
    if request.method == 'POST':
        try:
            book_review = BookReview.objects.get(pk=review_id)
        except BookReview.DoesNotExist:
            return HttpResponseNotFound("Book not found.")

        book_review.delete()

        response_data = {
            'status': True,
            'message': 'Review successfully deleted.',
        }

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({
            'status': False,
            'message': 'Failed deleting review',
        }, status=200)


def get_book_reviews_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    try:
        book_review = BookReview.objects.filter(book__id=book_id)
        print("miau")
    except BookReview.DoesNotExist:
        book_review = None
        print("miau1")

    data = [{
        'pk': review.pk,
        'user': review.user.username,
        'content': review.content,
        'stars': review.stars,
        'date_added': review.date_added

    } for review in book_review]
    # return HttpResponse(serializers.serialize('json', book_review))
    return JsonResponse({'book_review': data})