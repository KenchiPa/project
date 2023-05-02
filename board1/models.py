from django.db import models
from datetime import datetime, timedelta
from django.db.models import F, IntegerField
from django.db.models import CharField, IntegerField
from django.dispatch import receiver
from common.models import CommonModel

from common.fields import MarkdownField
from django.utils import timezone
from django.db.models.functions import Substr, Cast
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete



# Create your models here.

class Board1(CommonModel):

    """ Board1 게시판 """

    # PERMISSION_CHOICES = (
    #     ('1', "Board1"),
    #     ('2', "Board2"),
    #     ('3', "Board3"),
    # )
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='board1')
    view_count = models.PositiveIntegerField(default=0)
    # permission = models.CharField(max_length=1, choices=PERMISSION_CHOICES)
    # board_mapping = models.ForeignKey(BoardMapping, on_delete=models.CASCADE, related_name='board1', null=True, blank=True)

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def __str__(self):
        return self.title
    

class AdditionalField(models.Model):
    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=20)
    board = models.ForeignKey(Board1, on_delete=models.CASCADE)
