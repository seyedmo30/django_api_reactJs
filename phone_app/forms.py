from django import forms
from .models import Phone

class DocumentForm(forms.Form):
    document = forms.ImageField(required=False)


class SearchForm(forms.Form):
    query = forms.CharField()


from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )
