from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import (
    LectureSerializer,
    AssignmentSerializer,
    ProfessorImageSerializer,
    StudentVideoSerializer,
    StudentImageSerializer,
)
from .permissions import IsOwnerOrReadOnly
from .models import Lecture, Assignment, ProfessorImage, StudentVideo, StudentImage
from django.http.response import JsonResponse

#Lecture
class LectureList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    serializer_class = LectureSerializer

    def perform_create(self, serializer):
        serializer.save(professor=self.request.user)
    
    def get_queryset(self):
        #when user is professor
        if self.request.user.is_staff == True:
            return Lecture.objects.filter(professor_id=self.request.user.id)
        #when user is student
        return Lecture.objects.filter(students=self.request.user.id)
        
class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    serializer_class = LectureSerializer

#Assignment
class AssignmentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AssignmentSerializer
    
    def get_queryset(self, **kwargs):
        return Assignment.objects.filter(lecture=self.kwargs['lecture'])

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AssignmentSerializer

#professor image
class ProfessorImageList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProfessorImageSerializer
    
    def get_queryset(self, **kwargs):
        return ProfessorImage.objects.filter(assignment=self.kwargs['assignment'])

class ProfessorImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfessorImage.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProfessorImageSerializer

#student video
#svideo list/get 아직은 필요없음
class StudentVideoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentVideoSerializer

    def get_queryset(self, **kwargs):
        return StudentVideo.objects.filter(assignment=self.kwargs['assignment'])
        
class StudentVideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentVideo.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentVideoSerializer

#student image
class StudentImageList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentImageSerializer

    def get_queryset(self, **kwargs):
        return StudentImage.objects.filter(student_video=self.kwargs['student_video'])
        
class StudentImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentImage.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentImageSerializer