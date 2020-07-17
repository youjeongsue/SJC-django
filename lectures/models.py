from django.db import models

class Lecture(models.Model):
    lecturename = models.CharField(max_length=100)
    professor = models.ForeignKey('accounts.User', related_name="professor_id", on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField('accounts.User', related_name="student_id", null=True, blank=True)

    def __str__(self):
        return self.lecturename

class Assignment(models.Model):
    assignmentname = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, related_name="assignments", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.assignmentname

class Comment(models.Model):
    assignment = models.ForeignKey(Assignment, related_name="comments", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.assignment