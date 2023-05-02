# from django.db import models
# from common.models import CommonModel
# from common.fields import MarkdownField
# from boardmapping.models import BoardMapping

# # Create your models here.

# class Board3(CommonModel):

#     """ Board3 게시판 """
#     title = models.CharField(max_length=100, default='DEFAULT')
#     content = models.TextField(default="DEFAULT")
#     author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='board3')
#     board_mapping = models.ForeignKey(BoardMapping, on_delete=models.CASCADE, related_name='board3', null=True)

#     def __str__(self):
#         return self.title
