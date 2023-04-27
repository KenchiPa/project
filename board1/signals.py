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
from .models import Board1


@receiver(pre_save, sender=Board1)
def update_month_number(sender, instance, **kwargs):
    if not instance.month_number:
        # 현재 시간을 이용해 YYYY-MM 형식의 문자열 생성
        month_str = timezone.now().strftime('%Y-%m')
        # 해당 월의 게시물 수 계산
        post_count = Board1.objects.filter(created_at__year=timezone.now().year,
                                          created_at__month=timezone.now().month).count()
        # month_number 필드 값 설정
        instance.month_number = int(month_str.replace('-', '') + '{:03d}'.format(post_count + 1))

@receiver(post_delete, sender=Board1)
def update_month_numbers(sender, instance, **kwargs):
    post_count = Board1.objects.filter(created_at__year=instance.created_at.year,
                                       created_at__month=instance.created_at.month).count()
    if post_count == 0:
        # 해당 월에 게시물이 없으면 월번호 업데이트 필요 없음
        return
    next_posts = Board1.objects.filter(created_at__year=instance.created_at.year,
                                        created_at__month=instance.created_at.month,
                                        month_number__gt=instance.month_number)
    Board1.objects.filter(month_number__gt=instance.month_number).update(month_number=F('month_number')-1)
    