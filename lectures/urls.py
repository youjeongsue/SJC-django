from django.urls import path
from .views import (
    LectureList,
    LectureDetail,
    AssignmentList,
    AssignmentDetail,
    ProfessorImageList,
    ProfessorImageDetail,
    StudentVideoList,
    StudentVideoDetail,
    StudentImageList,
    StudentImageDetail,
)

urlpatterns = [
    #lecture
    path("lectures/", LectureList.as_view()),
    path("lecture/<int:pk>/", LectureDetail.as_view()),
    #assignment
    path("assignments/<int:lecture>/", AssignmentList.as_view()),
    path("assignment/<int:pk>/", AssignmentDetail.as_view()),
    #professor image
    path("pimages/<int:assignment>/", AssignmentList.as_view()),
    path("pimage/<int:pk>/", AssignmentDetail.as_view()),
    #student video
    path("svideos/<int:assignment>/", StudentVideoList.as_view()),
    path("svideo/<int:pk>/", StudentVideoDetail.as_view()),
    #student image
    path("simages/<int:student_video>/", StudentImageList.as_view()),
    path("simage/<int:pk>/", StudentImageDetail.as_view()),
]