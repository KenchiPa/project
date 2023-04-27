from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from board1.models import Board1
from board2.models import Board2
from board3.models import Board3
from boardmapping.models import BoardMapping


def index(request):
    # user = request.user
    # print('user : ', user)

    # # 해당 사용자의 BoardMapping 객체를 가져옴
    # board_mapping = BoardMapping.objects.get(user=user)
    # print('bpard_mapping : ', board_mapping)

    
    # # 각각의 게시판 모델에서 해당 매핑된 객체를 가져옴
    # board1 = Board1.objects.filter(board_mapping=board_mapping)
    # board2 = Board2.objects.filter(board_mapping=board_mapping)
    # board3 = Board3.objects.filter(board_mapping=board_mapping)
    # print('board1 : ', board1)
    # print('board2 : ', board2)
    # print('board3 : ', board3)
    # # 각각의 게시판 객체를 context에 담아서 렌더링
    # context = {
    #     'board1': board1,
    #     'board2': board2,
    #     'board3': board3,
    # }
    # return render(request, 'index.html', context)


    return render(request, 'index.html')




