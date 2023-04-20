from django.db import models
from django.utils import timezone

# Create your models here.

class CommonModel(models.Model):
    
    """  Common Model Definition  """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')  # 생성될 때만 시간이 저장, 이후에는 변경 X.
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')  # 저장될 때마다 현재 시간이 자동으로 저장.
    month_number = models.CharField(max_length=11, verbose_name='월번호')  # verbose_name= : 어드민패널에서의 이름을 설정.

    def save(self):
        today = timezone.now()  # 2023-04-20 04:50:27.200436+00:00
        year_month = today.strftime('%Y-%m')  # 2023-04
        count = CommonModel.objects.filter(month_number__startswith=year_month).count() + 1  # 해당 월에 생성된 객체의 수 + 1
        self.month_number = f"{year_month}-{count:03d}"  # 2023-04-001
        super(CommonModel, self).save()

    class Meta:
        abstract = True