from django import forms
from .models import Article



class PostcreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content"]