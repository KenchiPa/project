from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from .forms import MyLoginForm
from users.models import User
from mappingboards.models import UserBoard



# from .forms import SignUpForm

# Create your views here.

class MyLoginView(FormView):
    template_name = 'common/signin.html'
    form_class = MyLoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        User = get_user_model()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # user = User.objects.filter(username=username)
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, '아이디 또는 비밀번호가 일치하지 않습니다.')
            return super().form_invalid(form)



def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다!')
            return redirect('common:login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {'form': form})

def SignUpView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


