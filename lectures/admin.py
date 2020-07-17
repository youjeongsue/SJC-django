from django.contrib import admin
from .models import Lecture, Assignment, Comment

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(Comment)