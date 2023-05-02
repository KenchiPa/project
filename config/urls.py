"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    # Admin page path setting
    path("admin/", admin.site.urls),
 
    # Page
    path("", views.index, name='index'),
    # path("login/", views.login_view, name='login'),
    # path("logout/", views.logout_view, name='logout'),

    # Auth
    # path("api/v1/users/", include("users.urls")),

    # Board
    path("board1/", include("board1.urls")),
    path("board2/", include("board2.urls")),
    path("board3/", include("board3.urls")),

    # Common
    path("common/", include('common.urls')),

    # User
    path("users/", include('users.urls')),

]


# 404
handler404 = 'config.views.custom_page_not_found_view'
