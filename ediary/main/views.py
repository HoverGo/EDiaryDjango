from django.shortcuts import render
from .models import *


# Main


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


# News


def news(request):
    news_data = {}
    news = News.objects.all()
    news_data["news"] = news
    return render(request, "main/news.html", news_data)


# Schedule


def schedule(request):
    return render(request, "main/schedule.html")
