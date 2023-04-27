from django import forms
from .models import Board1

class Board1Form(forms.ModelForm):
    class Meta:
        model = Board1
        fields = ('title', 'content')
        # , 'author', 'board_mapping', 'month_number'

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)