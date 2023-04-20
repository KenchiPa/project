from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom User
class User(AbstractUser):
    avatar = models.ImageField(
        blank=True,  # Form에서 필드가 필수적이지 않게한다. 
    )