from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, change_password, MyLoginView

app_name = 'common'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='common/signin.html'), name='login'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('signup/', SignUpView, name='signup'),
]

