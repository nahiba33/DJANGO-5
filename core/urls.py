from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path("", home__view, name="home"),
    path("about/", about__view, name="about"),
    path("our__articles", our__articles, name="our__articles"),
    path("my__articles", my__articles, name="my__articles"),
    path("contact", contact__view, name="contact"),
    path("account/", include("account.urls")),
    path('admin/', admin.site.urls),
]