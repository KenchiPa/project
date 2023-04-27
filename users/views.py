from django.shortcuts import render
from django.db.models import Q
from users.models import User, UserLoginHistory
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializers

# Create your views here.

def user_list(request):
    """ 사용자 조회 페이지 GET """
    users = User.objects.order_by('username')
    paginator = Paginator(users, 8) # 페이지당 10개의 게시물

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'common/user_list.html', {'users': page_obj})

def search(request):
    query = request.GET.get('search')
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | Q(name__icontains=query)
        )
        return render(request, 'common/user_list.html', {'users': users, 'query': query})
    else:
        users = User.objects.all()
        return render(request, 'common/user_list.html', {'users': users})
    
def history_list(request):
    """ 사용자 히스토리 조회 페이지 GET """
    users = UserLoginHistory.objects.order_by('-login_datetime')
    paginator = Paginator(users, 8) # 페이지당 10개의 게시물
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'common/user_history_list.html', {'users': page_obj})

def history_search(request):
    """ 사용자 히스토리 검색 """
    query = request.GET.get('search')
    if query:
        users = UserLoginHistory.objects.order_by('-login_datetime').filter(
            Q(user__username__icontains=query) | Q(login_datetime__icontains=query) | Q(login_ip__icontains=query) | Q(user__name__icontains=query)
            | Q(access_site__icontains=query) | Q(status__icontains=query)
        )
        paginator = Paginator(users, 8) # 페이지당 10개의 게시물
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'common/user_history_list.html', {'users': page_obj, 'query': query})
    else:
        users = UserLoginHistory.objects.order_by('-login_datetime')
        paginator = Paginator(users, 8) # 페이지당 10개의 게시물
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'common/user_history_list.html', {'users': page_obj})
        
