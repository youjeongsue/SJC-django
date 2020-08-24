from rest_framework import serializers
from .models import Lecture, Assignment, Student_video, Comment

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id','lecturename','image','professor','students']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'assignmentname', 'lecture', 'professor_video', 'student_video']

class StudentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_video
        fields = ['id', 'student', 'student_video']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'assignment', 'contents', 'timestamp']