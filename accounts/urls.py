from django.urls import path
from .views import (
    RegistrationAPI,
    LoginAPI,
    UserAPI
)

urlpatterns = [
    #account
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),

    #Student
]