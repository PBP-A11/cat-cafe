from django.contrib.auth.forms import UserCreationForm
from main.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "date_of_birth"]