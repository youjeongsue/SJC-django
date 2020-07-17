from django.db import models

class Lecture(models.Model):
    lecturename = models.CharField(max_length=100)
    professor = models.ForeignKey('accounts.User', related_name="professor_id", on_delete=models.CASCADE, blank=True)
    students = models.ManyToManyField('accounts.User', related_name="student_id", blank=True)

    def __str__(self):
        return self.lecturename

class Assignment(models.Model):
    assignmentname = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, related_name="assignments", on_delete=models.CASCADE)
    professor_video = models.FileField(blank=True)
    student_video = models.ManyToManyField('Student_video', related_name="student_videos", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.assignmentname

class Student_video(models.Model):
    student = models.ForeignKey('accounts.User', related_name="videos", on_delete=models.CASCADE)
    student_video = models.FileField(blank=True)

    def __str__(self):
        return self.student_video.name

class Comment(models.Model):
    assignment = models.ForeignKey(Assignment, related_name="comments", on_delete=models.CASCADE)
    contents = models.CharField(max_length=300)
    timestamp = models.TimeField()

    def __str__(self):
        return self.assignment