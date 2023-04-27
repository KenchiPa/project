
from django.urls import path
from . import views

app_name = 'users'

# users/
urlpatterns = [
    path('list/', views.user_list, name='user_list'),
    path('search/', views.search, name='search'),
    path('history/', views.history_list, name='history_list'),
    path('history_search/', views.history_search, name='history_search'),
]