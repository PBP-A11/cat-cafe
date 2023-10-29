from django.contrib.auth.forms import UserCreationForm
from main.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 125px;'})
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 125px;'})
    )
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    date_of_birth = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    fav_color = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 255px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 255px;'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "date_of_birth", "fav_color"]