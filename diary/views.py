from django.shortcuts import render
from .models import DiaryRecord

# Diary pages


def diary(request):
    data = {
        "title": "Дневник",
    }
    diary_records = DiaryRecord.objects.filter(user=request.user)

    data["diary_records"] = diary_records
    return render(request, "diary/diary.html", data)