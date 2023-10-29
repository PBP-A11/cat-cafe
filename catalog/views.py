from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse
import requests
from django.shortcuts import render
from dotenv import load_dotenv
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
import os
from catalog.models import Book
from main.models import BookReview
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def catalog(request):
    return render(request, "katalog.html")


def search_books(request, query):
    # Ganti 'YOUR_API_KEY' dengan API key Anda
    load_dotenv()
    max_result = 40
    # Membuat permintaan ke Google Books API
    url = f"https://www.googleapis.com/books/v1/volumes?q=inpublisher:{query}&key={os.getenv('api_key')}&maxResults={max_result}"
    response = requests.get(url)

    # Periksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengambil data JSON dari respons
        data = response.json()
        # Mengambil item-item buku dari data
        items = data.get('items', [])
        # Anda dapat memproses item-item buku sesuai kebutuhan
        return JsonResponse(items, safe=False)
    else:
        # Jika permintaan gagal, Anda bisa mengembalikan pesan kesalahan
        return JsonResponse({'error': 'Gagal dalam mengambil data'}, status=500)
    
def get_books_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize('json', data),
        content_type="application/json")

@csrf_exempt
def add_book_reviews_ajax(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(book_id = book_id)
        user = request.POST.get("user")
        content = request.POST.get("content")
        stars = request.POST.get("stars")
        date_added = request.user

        new_book_review = BookReview(book = book, user = user, content = content, stars = stars, date_added = date_added)
        new_book_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_book_reviews_json(request, book_id):
    book_review = BookReview.objects.filter(book_id = book_id)
    return HttpResponse(serializers.serialize('json', book_review))