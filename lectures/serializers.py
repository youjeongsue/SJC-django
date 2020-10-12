from rest_framework import serializers
from .models import Lecture, Assignment, ProfessorImage, StudentVideo, StudentImage

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id','lecturename','image','professor','students']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'assignmentname', 'score', 'lecture', 'p_video']

class ProfessorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorImage
        fields = ['id', 'assignment', 'p_image']

class StudentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentVideo
        fields = ['id', 'student', 'assignment', 's_video']

class StudentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentImage
        fields = ['id', 'student_video', 's_image_path', 'comment']