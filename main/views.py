from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from main.models import User, Book
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from main.forms import RegisterUserForm

from django.contrib.auth import authenticate, login, logout


"""
CTT. (hapus kalo udah selesai, update sesuai kebutuhan)
1. jika ingin hanya beberapa tipe user yang menjalankan fungsi tertentu, gunakan @permission_required diatas fungsi tersebut
eg.

@permission_required('main.permissionPadaModels')
def ....

permissionPadaModels bisa diatur di models.py member/admin sesuai kebutuhan pada:
eg.
permissions = [
            ("permissionPadaModels, "contoh aja"),
        ]

2. bisa juga pengecekan jenis user dengan user.user_type untuk tau role user ADMIN/MEMBER, ctt."user" tergantung var yang digunakan untuk nyimpan.
"""

@login_required(login_url='/login')

def main(request):
    return render(request, "main.html")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                date_of_birth=form.cleaned_data["date_of_birth"],
            )

            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect('main:login')           
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:main')
        else:
            error_message = 'Sorry, incorrect username or password. Please try again.'
    context = {'error_message': error_message}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('main:login')


def get_books_json_preview(request):
    data = Book.objects.all()[:2]  # Mengambil hanya 4 data pertama
    return HttpResponse(serializers.serialize('json', data),
        content_type="application/json")