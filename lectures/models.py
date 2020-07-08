from django.db import models

class Lecture(models.Model):
    classname = models.CharField(max_length=100)
    professor = models.ForeignKey('accounts.User', related_name="lectures", on_delete=models.CASCADE, null=True)

class Assignment(models.Model):
    assignmentname = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, related_name="assignments", on_delete=models.CASCADE, null=True)
