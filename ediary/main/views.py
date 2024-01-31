from django.shortcuts import render

# Info pages


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def schedule(request):
    return render(request, "main/schedule.html")
