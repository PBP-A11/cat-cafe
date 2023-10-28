from django.shortcuts import render
from main.models import Book, User
from django.contrib.auth.decorators import login_required

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