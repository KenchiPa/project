from django.contrib.auth import get_user_model
from users.models import UserLoginHistory
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_login_failed

class SaveIpAddressMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response     

    @receiver(user_logged_in)
    def log_user_logged_in(sender, request, user, **kwargs):
        if request.path == '/common/login/':
            UserLoginHistory.objects.create(
                user=user,
                login_datetime=timezone.now(),
                login_ip=get_client_ip(request),
                access_site='Site',
                status="Success"
            )
        elif request.path == '/admin/login/':
            UserLoginHistory.objects.create(
                user=user,
                login_datetime=timezone.now(),
                login_ip=get_client_ip(request),
                access_site='Django',
                status="Success"
            )

    @receiver(user_login_failed)
    def log_user_login_failed(sender, credentials, request, **kwargs):
        if request.path == '/common/login/':
            try:
                user = get_user_model().objects.get(username=credentials['username'])
            except get_user_model().DoesNotExist:
                user = None
            UserLoginHistory.objects.create(
                user=user,
                login_datetime=timezone.now(),
                login_ip=get_client_ip(request),
                access_site='Site',
                status="False"
            )
        elif request.path == '/admin/login/':
            try:
                user = get_user_model().objects.get(username=credentials['username'])
            except get_user_model().DoesNotExist:
                user = None
            UserLoginHistory.objects.create(
                user=user,
                login_datetime=timezone.now(),
                login_ip=get_client_ip(request),
                access_site='Django',
                status="False"
            )

def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    

