from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from main.models import User, Book
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from main.forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count

@login_required(login_url='/login')
def mybooks(request):
    user = request.user
    if user.user_type == 'ADMIN':
        all_borrowed_books = Book.objects.filter(is_borrowed = True).values()
        all_member_user = User.objects.filter(user_type = 'MEMBER')
        users_book_count = User.objects.annotate(book_count=Count('book'))
        context = {
            'user': user,
            'member_users': all_member_user,
            'books': all_borrowed_books,
            'users_book_count': users_book_count,
        }
        return render(request, 'listpeminjam.html', context)
    else :
        books = Book.objects.filter(borrower=request.user)
        context ={
            'books': books
        }
        return render(request, "mybooks.html", context)
        

def get_mybooks_json(request):
    print(request.user)
    data = Book.objects.filter(borrower=request.user)
    return HttpResponse(serializers.serialize('json', data),
        content_type="application/json")

def get_mybooks_json_flutter(request, username):
    # Retrieve the user object based on the provided username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # Handle the case where the user doesn't exist
        return HttpResponse(status=404)

    # Filter books based on the obtained user object
    data = Book.objects.filter(borrower=user)
    
    # Serialize and return the data
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")


def book_return(request, id):
    if request.method == 'GET':
        data = Book.objects.get(pk=id)
        data.is_borrowed = False
        data.borrower = None
        data.save()
        return HttpResponse(b"SUCCESS", status=200)
    return HttpResponseNotFound()

def promote_to_admin(request, id):
    print('tes')
    user = User.objects.get(pk=id)
    user_books = Book.objects.filter(borrower=user)
    for book in user_books:
        book.is_borrowed = False
        book.borrower = None
        book.save()
    user.user_type = 'ADMIN'
    user.save()
    return redirect('mybooks:mybooks')