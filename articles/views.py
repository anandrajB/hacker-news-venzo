from django.shortcuts import render
from .models import Article
# Create your views here.


def index(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"index.html",{"articles":articles})