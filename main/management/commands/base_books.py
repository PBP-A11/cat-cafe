from django.core.management.base import BaseCommand
from main.models import Book
import requests

class Command(BaseCommand):
    help = 'add books'

    def handle(self, *args, **options):

        API_KEY = "AIzaSyBGjXMDTu7LZoIR7pHj01aDW_-zLp4UTIk"

        def search_books(query):
            base_url = 'https://www.googleapis.com/books/v1/volumes'
            params = {'q': query, 'key': API_KEY}

            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                return data['items']
            else:
                print(f"Error: {response.status_code}")
                return None

        # Example usage
        search_query = 'Python programming'
        results = search_books(search_query)

        if results:
            for book in results:
                Book.objects.create(title=book['volumeInfo'].get('title', 'N/A'),
                                    author=book['volumeInfo'].get('authors', ['N/A'])[0],
                                    date_published=book['volumeInfo'].get('publishedDate', 'N/A'),
                                    image_link=book['volumeInfo'].get('imageLinks', {}).get('thumbnail', 'N/A'),
                                    preview_link=book['volumeInfo'].get('previewLink', 'N/A'),
                                    rating=str(book['volumeInfo'].get('averageRating', 'N/A')),
                                    description=book['volumeInfo'].get('description', 'N/A'),
                                    category=book['volumeInfo'].get('categories', ['N/A'])[0])

        self.stdout.write(self.style.SUCCESS('Books added successfully.'))
