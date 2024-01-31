from .models import *
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"

        widgets = {
            "name": TextInput(
                attrs={"class": "form-control", "placeholder": "Название статьи"}
            ),
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Анонс статьи"}
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Текст статьи"}
            ),
        }
