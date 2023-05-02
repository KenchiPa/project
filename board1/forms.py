from django import forms
from .models import Board1

class Board1Form(forms.ModelForm):
    class Meta:
        model = Board1  # 사용할 모델
        fields = ('title', 'content')  # Board1Form에서 사용할 Board1 모델의 속성
        # , 'author', 'board_mapping', 'month_number'

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            fields = Board1.objects.all()
            for field in fields:
                if field.type == 'text':
                    self.fields[field.name] = forms.CharField()
                elif field.type == 'textarea':
                    self.fields[field.name] = forms.CharField(widget=forms.Textarea)
                elif field.type == 'image':
                    self.fields[field.name] = forms.ImageField()
                elif field.type == 'select':
                    self.fields[field.name] = forms.ChoiceField(choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2')])