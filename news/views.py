from django.shortcuts import render, redirect
from .forms import *
from .services.services import get_all_news, get_one_news, delete_one_news


def news(request):
    """
    Вывод всех новостей из базы данных на страницу

    """
    data = {}
    data["title"] = "Новости"
    data["news"] = get_all_news()
    print(data)
    return render(request, "news/news.html", data)


def news_add(request):
    user = request.user

    if user.is_superuser:
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
            "title": "Добавить новость",
            "form": form,
            "error": error,
        }
        return render(request, "news/news_add.html", data)
    else:
        return render(request, "main/index.html", data)


def news_details(request, id):
    """
    Обработка страницы с конкретной новостью

    """
    data = {}
    news = get_one_news(id)
    data["title"] = news.name
    data["news"] = news
    print(data)
    return render(request, "news/news_details.html", data)


def news_delete(request, id):
    delete_one_news(id)
    return redirect("news")
