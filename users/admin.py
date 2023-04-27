from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserLoginHistory

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 관리자 페이지에서 model의 field가 보이는 순서를 설정할 수 있게 해준다.(섹션에 넣어서 제목을 붙일 수 있다.)
    # 반대로 fields = 보여주기만 할 수 있다.
    fieldsets = (
        (
            "사용자 정보", {
                "fields": (
                    "username", 
                    "name",  
                    "gender", 
                    "email", 
                    "phone_number",
                    "is_manager",
                    "access_site"
                    # "can_see", 
                ),
                "classes": ("wide",),
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
                "classes": ("wide",),
            },
        ),
        (
            "중요한정보", {
                "fields": (
                    "last_login", 
                    "date_joined",
                ),
                "classes": ("wide",),
            },
        ),
    )
    # 사용자 추가할 때 보이는 필드
    # add_fieldsets = (
    #         (
    #             None,
    #             {
    #                 "classes": ("wide",),
    #                 "fields": ("username", 
    #                 "name", 
    #                 "gender", 
    #                 "email", 
    #                 "phone_number", 
    #                 "profile_picture",
    #                 # "can_see",
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",),
    #             },
    #         ),
    #     )
    # 사용자 리스트를 표시할 때 보이는 Colum 설정
    list_display = (
        "username",
        "name",
        "gender",
        "email",
        "is_manager",
        "is_staff",
        "access_site",
        # "can_see"
    )


@admin.register(UserLoginHistory)
class Board1Admin(admin.ModelAdmin):
    pass
   