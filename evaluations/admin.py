from django.contrib import admin
from .models import Subject, Number, Letter, Mark, SchoolClass, TeacherSubject, ClassAffilation, StudentRatingForItem, SubjectAffilation

admin.site.register(Subject)
admin.site.register(Number)
admin.site.register(Letter)
admin.site.register(Mark)
admin.site.register(SchoolClass)
admin.site.register(TeacherSubject)
admin.site.register(ClassAffilation)
admin.site.register(StudentRatingForItem)
admin.site.register(SubjectAffilation)