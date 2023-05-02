from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# from board1.models import Board1

# Create your models here.

# Custom User
class User(AbstractUser): 
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    PERMISSION_CHOICES = (
        ('0', "No Board"),
        ('1', "Board1"),
        ('2', "Board2"),
        ('3', "Board3"),
        ('4', "All Board"),
    )
    # Not Use
    first_name = models.CharField(max_length=30, editable=False)  # 성
    last_name = models.CharField(max_length=30, editable=False)  # 이름

    # Use
    username = models.CharField(max_length=30, unique=True)  # 유저네임
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)  # 성별
    email = models.EmailField(unique=True)  # 이메일 주소
    phone_number = models.CharField(max_length=11, null=True, blank=True)  # 휴대폰번호
    is_manager = models.BooleanField(default=False, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    access_site = models.CharField(max_length=150, default="DEFAULT")
    board_permissions = models.CharField(max_length=1,null=True, blank=True, choices=PERMISSION_CHOICES)
    # board1_permission = models.BooleanField(default=False)
    # board2_permission = models.BooleanField(default=False)
    # board3_permission = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print('DEF SAVE')
        super().save(*args, **kwargs)
        
        if self.board_permissions == '0':
            print('No Permission')
            free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
            if free_board3_group:
                self.groups.remove(free_board3_group)
            free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
            if free_board2_group:
                self.groups.remove(free_board2_group)
            free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
            if free_board1_group:
                self.groups.remove(free_board1_group)

        elif self.board_permissions == '1':
            print('board1')
            free_board1_group, created = Group.objects.get_or_create(name='Free Board1 Users')
            self.groups.add(free_board1_group)
            
            free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
            if free_board3_group:
                self.groups.remove(free_board3_group)
            free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
            if free_board2_group:
                self.groups.remove(free_board2_group)

        elif self.board_permissions == '2':
            print('board2')
            free_board2_group, created = Group.objects.get_or_create(name='Free Board2 Users')
            self.groups.add(free_board2_group)

            free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
            if free_board1_group:
                self.groups.remove(free_board1_group)
            free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
            if free_board3_group:
                self.groups.remove(free_board3_group)

        elif self.board_permissions == '3':
            print('board3')
            free_board3_group, created = Group.objects.get_or_create(name='Free Board3 Users')
            self.groups.add(free_board3_group)

            free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
            if free_board2_group:
                self.groups.remove(free_board2_group)
            free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
            if free_board1_group:
                self.groups.remove(free_board1_group)
            

        elif self.board_permissions == '4':
            print('board4')
            free_board3_group, created = Group.objects.get_or_create(name='Free Board3 Users')
            self.groups.add(free_board3_group)
            free_board2_group, created = Group.objects.get_or_create(name='Free Board2 Users')
            self.groups.add(free_board2_group)
            free_board1_group, created = Group.objects.get_or_create(name='Free Board1 Users')
            self.groups.add(free_board1_group)

            # free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
            # if free_board3_group:
            #     self.groups.remove(free_board3_group)
            # free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
            # if free_board2_group:
            #     self.groups.remove(free_board2_group)
            # free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
            # if free_board1_group:
            #     self.groups.remove(free_board1_group)        
        








        # if self.board_permissions == '0':
        #     print('No Permission')
        #     free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
        #     if free_board3_group:
        #         self.groups.remove(free_board3_group)
        #     free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
        #     if free_board2_group:
        #         self.groups.remove(free_board2_group)
        #     free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
        #     if free_board1_group:
        #         self.groups.remove(free_board1_group)
        # if self.board_permissions == '1':
        #     print('board1')
        #     free_board1_group, created = Group.objects.get_or_create(name='Free Board1 Users')
        #     self.groups.add(free_board1_group)
        # else:
        #     print('board1 X')
        #     free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
        #     if free_board1_group:
        #         self.groups.remove(free_board1_group)

        # if self.board_permissions == '2':
        #     print('board2')
        #     free_board2_group, created = Group.objects.get_or_create(name='Free Board2 Users')
        #     self.groups.add(free_board2_group)
        # else:
        #     print('board2 X')
        #     free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
        #     if free_board2_group:
        #         self.groups.remove(free_board2_group)

        # if self.board_permissions == '3':
        #     print('board3')
        #     free_board3_group, created = Group.objects.get_or_create(name='Free Board3 Users')
        #     self.groups.add(free_board3_group)
        # else:
        #     print('board3 X')
        #     free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
        #     if free_board3_group:
        #         self.groups.remove(free_board3_group)
        # if self.board_permissions == '4':
        #     print('board4')
        #     free_board3_group, created = Group.objects.get_or_create(name='Free Board3 Users')
        #     self.groups.add(free_board3_group)
        #     free_board2_group, created = Group.objects.get_or_create(name='Free Board2 Users')
        #     self.groups.add(free_board2_group)
        #     free_board1_group, created = Group.objects.get_or_create(name='Free Board1 Users')
        #     self.groups.add(free_board1_group)
        # else:
        #     print('board4 X')
        #     free_board3_group = Group.objects.filter(name='Free Board3 Users').first()
        #     if free_board3_group:
        #         self.groups.remove(free_board3_group)
        #     free_board2_group = Group.objects.filter(name='Free Board2 Users').first()
        #     if free_board2_group:
        #         self.groups.remove(free_board2_group)
        #     free_board1_group = Group.objects.filter(name='Free Board1 Users').first()
        #     if free_board1_group:
        #         self.groups.remove(free_board1_group)        
        


        

        
        # if self.board_permissions:
        #     free_board1_group, created = Group.objects.get_or_create(name='Free Board1 Users')
        #     self.groups.add(free_board1_group)
       
        # elif self.board2_permission:
        #     free_board2_group, created = Group.objects.get_or_create(name='Free Board2 Users')
        #     self.groups.add(free_board2_group)
       
        # elif self.board3_permission:
        #     free_board3_group, created = Group.objects.get_or_create(name='Free Board3 Users')
        #     self.groups.add(free_board3_group)
        
        #super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class UserLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    login_datetime = models.DateTimeField(auto_now_add=True)
    login_ip = models.CharField(max_length=20)
    access_site = models.CharField(max_length=150, default="DEFAULT")
    status = models.CharField(max_length=150, null=True, blank=True)


