from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse
import requests
from django.shortcuts import render
from dotenv import load_dotenv
import os

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
    
