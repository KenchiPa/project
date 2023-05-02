from django.db import models
from users.models import User
from board1.models import Board1
# Create your models here.

class UserBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board1, on_delete=models.CASCADE)