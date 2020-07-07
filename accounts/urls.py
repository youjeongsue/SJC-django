from django.conf.urls import url
from .views import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
]