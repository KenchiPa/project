from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from board1.models import Board1

# Create your models here.

# Custom User
class User(AbstractUser): 
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # Not Use
    first_name = models.CharField(max_length=30, editable=False)  # 성
    last_name = models.CharField(max_length=30, editable=False)  # 이름

    # Use
    username = models.CharField(max_length=30, unique=True)  # 유저네임
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)  # 성별
    email = models.EmailField(unique=True)  # 이메일 주소
    phone_number = models.CharField(max_length=11, null=True, blank=True)  # 휴대폰번호
    is_manager = models.BooleanField(default=False, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    access_site = models.CharField(max_length=150, default="DEFAULT")
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # 사용자 프로필 사진

    def __str__(self):
        return self.username
    
class UserLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    login_datetime = models.DateTimeField(auto_now_add=True)
    login_ip = models.CharField(max_length=20)
    access_site = models.CharField(max_length=150, default="DEFAULT")
    status = models.CharField(max_length=150, null=True, blank=True)
