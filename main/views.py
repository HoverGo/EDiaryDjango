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
        "title": "Расписание",
    }
    return render(request, "main/schedule.html", data)
