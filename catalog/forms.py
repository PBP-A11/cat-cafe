from django.forms import ModelForm
from catalog.models import Book
from django import forms

class CreateBookForm(ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    author = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    description = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    category = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    date_published = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )
    image_link = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'style': 'width: 255px;'})
    )

    class Meta:
        model = Book
        fields = ["title","author", "description", "category", "date_published", "image_link"]