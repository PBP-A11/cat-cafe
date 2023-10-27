from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from main.models import User, Book
from django.core import serializers




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

def main(request):
    return render(request, "main.html")

def profile_user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "profile_user.html", context)

# def katalog(request):
#     books = Book.objects.all().values()
#     context = {'books': books}
#     return render(request, "katalog.html", context)
