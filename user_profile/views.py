import json
from django.shortcuts import render
from main.models import Book, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def user_profile(request):
    user = request.user
    if user.user_type == 'ADMIN':
        all_borrowed_books = Book.objects.filter(is_borrowed = True).values()
        all_member_user = User.objects.filter(user_type = 'MEMBER')
        context = {
            'user': user,
            'member_users': all_member_user,
            'books': all_borrowed_books,
        }
        return render(request, 'admin_profile.html', context)
    
    books = Book.objects.filter(borrower = user)
    context = {
        'user': user,
        'books': books,
    }
    
    return render(request, 'member_profile.html', context)

def get_user_json(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = request.user
            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
                'date_of_birth': user.date_of_birth,
                'user_type' : user.user_type,
            }
            return JsonResponse(user_data)
        else:
            return JsonResponse({'user_type': 'Not authenticated'})

def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        # user.username = request.POST.get("username")
        # user.date_of_birth = request.POST.get("date_of_birth")
        user.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt 
def edit_profile_flutter(request):
    if request.method == 'POST':
    
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return JsonResponse({"status": "success"}, status=200)

    return HttpResponseNotFound()

@csrf_exempt 
def edit_profile_flutter_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_username = data.get('username')
        
        # Memeriksa apakah username sudah ada dalam basis data
        existing_user = User.objects.filter(username=new_username).exists()

        if existing_user:
            # Username sudah ada, kirim respons bahwa username sudah digunakan
            return JsonResponse({"status": "error", "message": "Username sudah digunakan"}, status=400)

        # Username belum ada, lanjutkan untuk menyimpan perubahan
        user = request.user
        user.username = new_username
        user.save()

        return JsonResponse({"status": "success"}, status=200)

    return HttpResponseNotFound()
