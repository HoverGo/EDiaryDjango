from django.db import models
from users.models import User

class DiaryRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=2048)

    def __str__(self):
        return f"{self.name}: {self.date}"
    
    class Meta:
        verbose_name_plural = "Diary records"