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

@login_required(login_url='/login')
def mybooks(request):
    books = Book.objects.filter(borrower=request.user)
    context ={
        'books': books
    }
    return render(request, "mybooks.html", context)

def get_mybooks_json(request):
    data = Book.objects.filter(borrower=request.user)
    return HttpResponse(serializers.serialize('json', data),
        content_type="application/json")

def book_return(request, id):
    if request.method == 'GET':
        data = Book.objects.get(pk=id)
        data.is_borrowed = False
        data.borrower = None
        data.save()
        return HttpResponse(b"SUCCESS", status=201)
    return HttpResponseNotFound()