from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board1
from django.db.models import Q
from .forms import Board1Form
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_list(request):
    if request.method == "POST":
        posts = Board1.objects.order_by('-month_number').values('title','content','author__username','view_count','created_at','updated_at','month_number')
        data = list(posts)
        return JsonResponse(data, safe=False) 
    else:
        # posts = Board1.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
        posts = Board1.objects.order_by('-month_number')
        paginator = Paginator(posts, 8) # 페이지당 10개의 게시물
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'common/post_list.html', {'posts': page_obj})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_detail(request, pk):
    post = get_object_or_404(Board1, pk=pk)
    post.increase_view_count()  # 조회수 증가
    # comments = Comment.objects.filter(post=post).order_by('-created_at')
    return render(request, 'common/post_detail.html', {'post': post})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_new(request):
    if request.method == "POST":
        form = Board1Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board1:board1_detail', pk=post.month_number)
        else:
            print('is_valid Fail')
    else:
        form = Board1Form()
    return render(request, 'common/post_edit.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_edit(request, pk):
    post = get_object_or_404(Board1, pk=pk)
    if request.method == "POST":
        form = Board1Form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board1:board1_detail', pk=post.pk)
    else:
        form = Board1Form(instance=post)
    return render(request, 'common/post_edit.html', {'form': form, 'pk': post.pk})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_delete(request, pk):
    post = get_object_or_404(Board1, pk=pk)
    post.delete()
    return redirect('board1:board1_list')

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Free Board1 Users').exists())
def board1_search(request):
    query = request.GET.get('search')
    if query:
        posts = Board1.objects.order_by('-month_number').filter(
            Q(month_number__icontains=query) | Q(title__icontains=query) | Q(author__username__icontains=query) 
        )
        paginator = Paginator(posts, 8) # 페이지당 10개의 게시물
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'common/post_list.html', {'posts': page_obj, 'query': query})
    else:
        posts = Board1.objects.order_by('-month_number')
        paginator = Paginator(posts, 8) # 페이지당 10개의 게시물
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'common/post_list.html', {'posts': page_obj})

# def comment_new(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.save()
#             return redirect('post_detail', pk=comment.post.pk)
   


def update_order(request): 
    if request.method == 'POST':
        old_orders = Board1.objects.order_by('-month_number')
        old_orders = [str(post.month_number) for post in old_orders]
        new_orders = request.POST.getlist('new_orders[]')
        for i, new_order in enumerate(new_orders):
            old_order = old_orders[i]
            if old_order != new_order:
                # 이동할 데이터를 가져옵니다.
                obj = Board1.objects.get(month_number=old_order)
                # 이동할 위치를 계산합니다.
                new_index = new_orders.index(old_order)
                new_obj = Board1.objects.get(month_number=new_order)
                # 이동합니다.
                obj.month_number = new_order
                new_obj.month_number = old_order
                obj.save()
                new_obj.save()
                # old_orders 배열도 업데이트합니다.
                old_orders[new_index] = old_order       
        return HttpResponse('success')
