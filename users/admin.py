from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff',)
    
    fieldsets = (
        (
            "프로파일", 
            {
                "fields": (
                    'username', 
                    'first_name', 
                    'last_name', 
                    'gender', 
                    'email', 
                    'phone_number', 
                    'profile_picture',  
                    'last_login_ip', 
                ),
            },
        ),
        (
            "권한들", {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                # "classes": ("collapse",),
            },
        ),
        (
            "Important Dates", {
                "fields": (
                    "last_login", 
                    "date_joined"
                ),
                # "classes": ("collapse",),
            },
        ),
    )
