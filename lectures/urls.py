from django.urls import path
from .views import (
    LectureList,
    LectureDetail,
    AssignmentList,
    AssignmentDetail,
    CommentList,
    CommentDetail
)

urlpatterns = [
    path("lectures/", LectureList.as_view()),
    path("lecture/<int:pk>/", LectureDetail.as_view()),
    path("assignments/<int:lecture>/", AssignmentList.as_view()),
    path("assignment/<int:pk>/", AssignmentDetail.as_view()),
    path("comments/<int:assignment>/", CommentList.as_view()),
    path("comment/<int:pk>/", CommentDetail.as_view()),
]