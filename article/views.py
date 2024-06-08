from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def home__view(request):
    return render(request, "index.html")

def articles(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {'articles' : articles})

def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        # save() -> hemise commiti True olaraq qebul edir.
        messages.success(request, "Article is added.")
        return redirect("dashboard")
    context = {"form" : form}
    return render(request, "add_article.html", context)

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    return render(request, "dashboard.html", {'articles' : articles})

def about__view(request):
    return render(request, "about.html")

def contact__view(request):
    return render(request, "contact.html")

def article_detail(request, id):
    article = Article.objects.filter(id=id).first()
    context = {"article" : article}
    return render(request, "article_detail.html", context)