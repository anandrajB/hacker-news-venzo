from django.shortcuts import redirect, render

from articles.forms import PostcreationForm
from .models import Article
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":articles})
    cc  = Article.objects.all()

    return render(request,"index.html",{"articles":cc})


@login_required(login_url='login')
def addpost(request):
    form = PostcreationForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        posts = form.save(commit=False)
        posts.slug = slugify(posts.title)
        posts.author = request.user
        posts.save()

        c = messages.success(request,"new post added")

    return render(request,"upload.html",{"form":form})


  
def detail(request,slug):
    article = get_object_or_404(Article, slug=slug)
    cc = {"articles":article}
    return render(request,"details.html",cc)



@login_required(login_url = "user:login")
def updateArticle(request, slug):

    article = get_object_or_404(Article, slug=slug)
    form = PostcreationForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"updated success")
        return redirect("index.html")


    return render(request,"update.html",{"form":form})



# function for delelte and upote (9/10/21)

@login_required(login_url = "user:login")

def deleteArticle(request,slug):
    article = get_object_or_404(Article,slug=slug)

    article.delete()

    messages.success(request,"your post deleted success")

    return redirect("article:dashboard")