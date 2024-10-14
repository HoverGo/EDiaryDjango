from django.shortcuts import render

# Diary pages


def diary(request):
    data = {
        "title": "Дневник",
    }
    return render(request, "diary/diary.html", data)