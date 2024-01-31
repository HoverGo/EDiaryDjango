from django.shortcuts import render


def evaluations(request):
    return render(request, "main/evaluations.html")
