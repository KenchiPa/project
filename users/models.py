from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# Custom User
class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.CharField(max_length=30, unique=True)  # 유저네임
    first_name = models.CharField(max_length=30, blank=True)  # 성
    last_name = models.CharField(max_length=30, blank=True)  # 이름
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)  # 성별
    email = models.EmailField(unique=True)  # 이메일 주소
    phone_number = models.CharField(max_length=11, null=True, blank=True)  # 휴대폰번호
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # 사용자 프로필 사진
    is_staff = models.BooleanField(default=False)  # 관리자 여부
    last_login_ip = models.CharField(max_length=50, null=True, blank=True)  # 마지막 로그인 IP주소
    # last_login_at = models.DateTimeField(null=True, blank=True)  # 마지막 로그인 시간
    # created_at = models.DateTimeField(auto_now_add=True)  # 생성시간
    # updated_at = models.DateTimeField(auto_now=True)  # 수정시간

    def __str__(self):
        return self.username