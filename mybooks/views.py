from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, "mybooks.html")

def get_mybooks_json(request):
    data = Book.objects.filter(borrower=request.user)
    return HttpResponse(serializers.serialize('json', data),
        content_type="application/json")