
from django.urls import path
from . import views

# api/v1/users 
urlpatterns = [
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view())
]