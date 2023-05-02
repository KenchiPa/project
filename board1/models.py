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

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='board1')
    view_count = models.PositiveIntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     fields = self.fields.all()
    #     for field in fields:
    #         value = self.cleaned_data.get(field.name)
    #         AdditionalFieldData.objects.create(post=self, name=field.name, value=value)

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def __str__(self):
        return self.title
    

class AdditionalField(models.Model):
    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=20)

class AdditionalFieldData(models.Model):
    post = models.ForeignKey(Board1, on_delete=models.CASCADE, related_name='fields_data')
    field = models.ForeignKey(AdditionalField, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('post', 'field')


