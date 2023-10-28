
def user_context(request):
    return {
        'username': request.user.username,
    }