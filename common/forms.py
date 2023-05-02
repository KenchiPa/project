from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=150, required=True)
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    phone_number = forms.CharField(max_length=11, required=False)
    # board_permissions = forms.ChoiceField(choices=User.PERMISSION_CHOICES, required=False)
    is_manager = forms.BooleanField(initial=False, required=False)
    is_staff = forms.BooleanField(initial=False, required=False)
    is_superuser = forms.BooleanField(initial=False, required=False)
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'gender', 'email', 'phone_number', 'board_permissions', 'is_manager', 'is_staff', 'is_superuser')

class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)