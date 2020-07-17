from django.urls import path
from .views import (
    LectureList,
    LectureDetail,
)

urlpatterns = [
    path("lectures/", LectureList.as_view()),
    path("lectures/<int:pk>/", LectureDetail.as_view()),
]