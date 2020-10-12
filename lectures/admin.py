from django.contrib import admin
from .models import Lecture, Assignment, ProfessorImage, StudentVideo, StudentImage

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(ProfessorImage)
admin.site.register(StudentVideo)
admin.site.register(StudentImage)