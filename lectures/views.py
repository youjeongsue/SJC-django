from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import (
    LectureSerializer,
    AssignmentSerializer,
    CommentSerializer
)
from .permissions import IsOwnerOrReadOnly
from .models import Lecture, Assignment, Comment
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

#Comment
class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CommentSerializer

    def get_queryset(self, **kwargs):
        return Comment.objects.filter(assignment=self.kwargs['assignment'])
        
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CommentSerializer