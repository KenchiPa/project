from django.db import models
from django.utils import timezone

# Create your models here.

class CommonModel(models.Model):
    
    """  Common Model Definition  """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')  # 생성될 때만 시간이 저장, 이후에는 변경 X.
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')  # 저장될 때마다 현재 시간이 자동으로 저장.
    month_number = models.AutoField(primary_key=True)
    class Meta:
        abstract = True

# unique=True,
    