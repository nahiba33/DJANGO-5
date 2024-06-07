from django.shortcuts import render
from .models import Article

# Create your views here.
def home__view(request):
    return render(request, "index.html")

def our__articles(request):
    articles = Article.objects.all()
    return render(request, "our__articles.html", {'articles' : articles})

def my__articles(request):
    articles = Article.objects.all()
    return render(request, "my__articles.html", {'articles' : articles})

def about__view(request):
    return render(request, "about.html")

def contact__view(request):
    return render(request, "contact.html")