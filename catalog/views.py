import json
from django.shortcuts import redirect, render
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound
import requests
from django.shortcuts import render
from dotenv import load_dotenv
from django.http import HttpResponse
from django.core import serializers
import os
from catalog.forms import CreateBookForm
from catalog.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def catalog(request):
    return render(request, "katalog.html")


def search_books(request, query):
    # Ganti 'YOUR_API_KEY' dengan API key Anda
    load_dotenv()
    max_result = 40
    # Membuat permintaan ke Google Books API
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{query}&key={os.getenv('api_key')}&maxResults={max_result}"
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

def search_book(request):
    search_title = request.GET.get('searchTitle')
    search_author = request.GET.get('searchAuthor')
    search_category = request.GET.get('searchCategory')
    
    if search_title:
        books = Book.objects.filter(title__icontains=search_title)
        context = {'search': search_title, 'books': books}
    elif search_author:
        books = Book.objects.filter(author__icontains=search_author)
        context = {'search': search_author, 'books': books}
    elif search_category:
        books = Book.objects.filter(category__icontains=search_category)
        context = {'search': search_category, 'books': books}
    else:
        books = Book.objects.all()
        context = {'search': search_title, 'books': books}
    
    return render(request, 'katalog.html', context)

@csrf_exempt
@login_required
def book_borrowed(request, id):
    if request.method == 'GET':
        data = Book.objects.get(pk=id)
        data.is_borrowed = True
        data.borrower = request.user
        data.save()
        return HttpResponse(b"SUCCESS", status=201)
    return HttpResponseNotFound()

@csrf_exempt
# @login_required(login_url='/auth/login')
def book_borrowed_flutter(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            data = Book.objects.get(pk = id)
            if not data.is_borrowed:
                data.is_borrowed = True
                data.borrower = request.user
                data.save()
                return JsonResponse({"status": "success"}, status=200)
            
            return JsonResponse({"status": "error"}, status=400)
        
    return JsonResponse({"status": "not_login"}, status=401)

@csrf_exempt
def delete_book(request, id):
    if request.method == 'GET':
        data = Book.objects.get(pk=id)
        data.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

def add_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book = Book(
                title=form.cleaned_data["title"],
                author=form.cleaned_data["author"],
                description=form.cleaned_data["description"],
                category=form.cleaned_data["category"],
                date_published=form.cleaned_data["date_published"],
                image_link=form.cleaned_data["image_link"],
            )

            book.save()
            return redirect('main:main')           
    else:
        form = CreateBookForm()
    context = {'form': form}
    return render(request, 'addBook.html', context)


@csrf_exempt
def add_book_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        book = Book(
            title=data["title"],
            author=data["author"],
            description=data["description"],
            category=data["category"],
            date_published=data["date_published"],
            image_link=data["image_link"],
        )

        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_book_flutter(request, id):
    data = Book.objects.get(pk=id)
    data.delete()
    return JsonResponse({"message": "Data deleted successfully"}, status=200)
