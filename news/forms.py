from .models import News
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название статьи"}
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Анонс статьи"}
            ),
            "text": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Текст статьи"}
            ),
        }
