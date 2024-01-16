from django.urls import path
from . import views

urlpatterns = [
    path("", views.ashuri, name="ashuri"),
    path("login_user", views.login_user, name="login") 
]