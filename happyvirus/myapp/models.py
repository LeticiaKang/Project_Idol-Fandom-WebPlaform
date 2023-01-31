from django.db import models

#AbstractUser: 장고에서 제공하는 로그인 기능 사용하기 위한 모델
from django.contrib.auth.models import AbstractUser
# # Create your models here.

          #AbstractUser 상속: 장고에서 제공하는 유저에 관련된 모든 기능을 사용할 수 있게 됨
class User(AbstractUser):
    pass
    