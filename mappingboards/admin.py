from django.contrib import admin
from .models import UserBoard
# Register your models here.

@admin.register(UserBoard)
class Board1Admin(admin.ModelAdmin):
    pass

