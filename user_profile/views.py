from django.shortcuts import render
from main.models import Book, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers

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
    user = request.user
    user_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'date_of_birth': user.date_of_birth,
    }
    return JsonResponse(user_data)

def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.date_of_birth = request.POST.get("date_of_birth")
        user.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()