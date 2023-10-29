from django.contrib.auth.forms import UserCreationForm
from main.models import User
from django import forms
import datetime


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
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 255px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 255px;'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "date_of_birth"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        date_of_birth = cleaned_data.get("date_of_birth")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please make sure both passwords are the same.")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already in use. Please choose a different username.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email account is already in use. Please choose a different email.")

        try:
            datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            raise forms.ValidationError("Invalid date format. Date must be in YYYY-MM-DD format.")