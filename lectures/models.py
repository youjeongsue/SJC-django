from django.db import models

#lecture
class Lecture(models.Model):
    lecturename = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    professor = models.ForeignKey('accounts.User', related_name="professor_id", on_delete=models.CASCADE, blank=True)
    students = models.ManyToManyField('accounts.User', related_name="student_id", blank=True)

    def __str__(self):
        return self.lecturename

#assignment(professor video)
def p_video_upload_path(instance, filename):
    name, ext = filename.split('.')
    file_path = '{lecture_id}/{assignment_id}/prof/p_video.{ext}'.format(
        lecture_id=instance.lecture_id, assignment_id=instance.id, ext=ext)
    return file_path

class Assignment(models.Model):
    lecture = models.ForeignKey(Lecture, related_name="assignments", on_delete=models.CASCADE)
    assignmentname = models.CharField(max_length=100)
    score = models.IntegerField(null=True, blank=True)
    p_video = models.FileField(upload_to=p_video_upload_path, blank=True)

    def __str__(self):
        return self.assignmentname

#professor image
def p_image_upload_path(instance, filename):
    name, ext = filename.split('.')
    file_path = '{lecture_id}/{assignment_id}/prof/images/{name}.{ext}'.format(
        lecture_id=instance.assignment.lecture_id, assignment_id=instance.assignment_id, name=name, ext=ext)
    return file_path

class ProfessorImage(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='p_image', on_delete=models.CASCADE)
    p_image = models.ImageField(upload_to=p_image_upload_path, null=True, blank=True)

#student video
def s_upload_path(instance, filename):
    name, ext = filename.split('.')
    file_path = '{lecture_id}/{assignment_id}/{student_id}/s_video.{ext}'.format(
        lecture_id=instance.assignment.lecture_id, assignment_id=instance.assignment_id, student_id=instance.student_id, ext=ext)
    return file_path

class StudentVideo(models.Model):
    student = models.ForeignKey('accounts.User', related_name="videos", on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name='s_video', on_delete=models.CASCADE)
    s_video = models.FileField(upload_to=s_upload_path, null=True, blank=True)

    def __str__(self):
        return self.s_video.name

#student image
class StudentImage(models.Model): 
    student_video = models.ForeignKey(StudentVideo, related_name="comments", on_delete=models.CASCADE, null=True)
    s_image_path = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.comment