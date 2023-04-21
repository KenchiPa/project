from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from .signals import *

from .models import CustomUser

@receiver(user_logged_in)
def update_last_login_ip(sender, user, request, **kwargs):
    # only update for custom user model
    UserModel = get_user_model()
    if isinstance(user, UserModel):
        custom_user, created = CustomUser.objects.get_or_create(user=user)
        custom_user.last_login_ip = get_client_ip(request)
        custom_user.save()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip