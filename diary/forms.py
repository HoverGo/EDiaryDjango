from django import forms
from .models import DiaryRecord


class DiaryRecordForm(forms.ModelForm):
    class Meta:
        model = DiaryRecord
        fields = ("name", "text")

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Название записи"}),
            'text': forms.TextInput(attrs={"class": "form-control", "placeholder": "Текст записи"})
        }