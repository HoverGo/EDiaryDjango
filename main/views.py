from django.shortcuts import render

# Info pages


def index(request):
    data = {
        "title": "Главная страница",
    }
    return render(request, "main/index.html", data)


def about(request):
    data = {
        "title": "Про нас",
    }
    return render(request, "main/about.html", data)


def schedule(request):
    data = {
        "title": "Команда",
    }
    return render(request, "main/schedule.html", data)


def page_not_found(request, exception):
    render(request, "404.html", status=404)