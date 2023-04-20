from django.db import models
from common.models import CommonModel
from common.fields import MarkdownField

# Create your models here.

class Board1(CommonModel):

    """ Board1 게시판 """

    title = models.CharField(  # 제목
        max_length=200
    ) 
    author = models.ForeignKey(  # 작성자
        "users.User", 
        on_delete=models.CASCADE
    )     
    content = MarkdownField() # 내용

    # <div class="post-content">
    # {{ post.content.render }}
    # </div>

    # attachments = models.ManyToManyField(Attachment) # 첨부파일
    views = models.PositiveIntegerField(default=0) # 조회수



