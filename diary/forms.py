from django import forms
from .models import DiaryRecord


class DiaryRecordForm(forms.ModelForm):
    class Meta:
        model = DiaryRecord
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Название записи"}),
            'text': forms.TextInput(attrs={"placeholder": "Текст записи"})
        }