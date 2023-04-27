from django.urls import path
from . import views

app_name = 'board1'

# Default : localhost:8000/board1/
urlpatterns = [
    path('', views.board1_list, name='board1_list'),
    path('post/<int:pk>/', views.board1_detail, name='board1_detail'),
    path('post/new/', views.board1_new, name='board1_new'),
    path('post/<int:pk>/edit/', views.board1_edit, name='board1_edit'),
    path('post/<int:pk>/delete/', views.board1_delete, name='board1_delete'),
    path('search/', views.board1_search, name='post_search'),
    
    path('update_order/', views.update_order, name='update_order')

    
    # path('comment/new/', views.comment_new, name='comment_new'),
    # path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    # path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
