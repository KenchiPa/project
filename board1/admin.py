from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Board1)
class Board1Admin(admin.ModelAdmin):
    pass



