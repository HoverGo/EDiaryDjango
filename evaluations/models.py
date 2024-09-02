from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Subject(models.Model):
    """
    Предметы в школе
    """
    subject = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.subject

class Number(models.Model):
    """
    Цифра класса
    """
    number = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(11),
        ]
    )
    
    def __str__(self):
        return str(self.number)
    
class Letter(models.Model):
    """
    Буква класса
    """
    letter = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.letter

class Mark(models.Model):
    """
    Оценка, которую можно выставить за предмет
    """
    number = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    def __str__(self):
        return str(self.number)

class SchoolClass(models.Model):
    """
    Школьные классы (соотношение номера и буквы)
    """
    number_of_class = models.ForeignKey(Number, on_delete=models.SET_NULL, blank=True, null=True)
    letter_of_class = models.ForeignKey(Letter, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f"{self.number_of_class}{self.letter_of_class}"
    
    class Meta:
        verbose_name_plural = "School classes"

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    """
    Предметы, по которым учитель может ставить оценки
    """

    def __str__(self):
        return f"Teacher: {self.teacher}, Subject: {self.subject}"

class ClassAffilation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, blank=True, null=True)
    """
    Принадлежность учителя или ученика определённому классу
    """

    def __str__(self):
        return f"User: {self.user}, Class: {self.school_class}"

class StudentRatingForItem(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    """
    Оценка ученика по определённому предмету
    """
    
    def __str__(self):
        return f"Student {self.student}, Got {self.mark} in {self.subject}"

class SubjectAffilation(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    """
    Принадлежность предмета определённому классу
    """
    def __str__(self):
        return f"{self.school_class} {self.subject}"



