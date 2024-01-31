from django.shortcuts import render, redirect
from .models import *
from .forms import *


def news(request):
    news_data = {}
    news = News.objects.all()
    news_data["news"] = news
    return render(request, "news/news.html", news_data)


def news_add(request):
    error = ""
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            error = "Неверная форма"

    form = NewsForm()

    data = {
        "form": form,
        "error": error,
    }
    return render(request, "news/news_add.html", data)
