from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path("", home__view, name="home"),
    path("about/", about__view, name="about"),
    path("articles", articles, name="articles"),
    path("dashboard", dashboard, name="dashboard"),
    path("add_article", add_article, name="add_article"),
    path("article_detail/<int:id>", article_detail, name="article_detail"),
    path("contact", contact__view, name="contact"),
    path("account/", include("account.urls")),
    path('admin/', admin.site.urls),
]