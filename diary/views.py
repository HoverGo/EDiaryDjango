from django.shortcuts import render, redirect
from .models import DiaryRecord
from .forms import DiaryRecordForm
from .services.services import save_form

# Diary pages


def diary(request):
    data = {
        "title": "Дневник",
    }
    if request.user.is_authenticated:
        diary_records = DiaryRecord.objects.filter(user=request.user)
        data["records"] = diary_records
        print(data["records"])
    return render(request, "diary/diary.html", data)


def diary_add(request):
    error = ""
    if request.method == "POST":
        form = DiaryRecordForm(request.POST)
        if form.is_valid:
            save_form(request, form)
            return redirect("diary")
        else:
            error = "Неверная форма"

    form = DiaryRecordForm()
    data = {
        "title": "Добавить новость",
        "form": form,
        "error": error,
    }

    return render(request, "diary/add_diary.html", data)
