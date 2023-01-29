from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("response/", views.data_response, name="response"),
]
