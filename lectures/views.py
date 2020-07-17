from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import LectureSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Lecture
from django.http.response import JsonResponse

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