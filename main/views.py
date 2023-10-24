from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from main.models import User, Book

# Create your views here.
def main(request):
    return render(request, "main.html")

def profile_user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "profile_user.html", context)

def katalog(request):
    books = Book.objects.all().values()
    context = {'books': books}
    return render(request, "katalog.html", context)
