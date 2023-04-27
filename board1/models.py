from django.db import models
from datetime import datetime, timedelta
from django.db.models import F, IntegerField
from django.db.models import CharField, IntegerField
from django.dispatch import receiver
from common.models import CommonModel
from boardmapping.models import BoardMapping
from common.fields import MarkdownField
from django.utils import timezone
from django.db.models.functions import Substr, Cast
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete



# Create your models here.

class Board1(CommonModel):

    """ Board1 게시판 """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='board1')
    view_count = models.PositiveIntegerField(default=0)
    # board_mapping = models.ForeignKey(BoardMapping, on_delete=models.CASCADE, related_name='board1', null=True, blank=True)

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def __str__(self):
        return self.title
