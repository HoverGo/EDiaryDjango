from django.db import models


class News(models.Model):
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField(max_length=2048, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.title}"

    class Meta:
        verbose_name_plural = "News"
