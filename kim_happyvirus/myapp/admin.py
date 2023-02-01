from django.contrib import admin

#현재 같은 디렉터리에서 models안에 있는 User 불러오기
from .models import User
# Register your models here.

#만든 User모델을 등록하기
admin.site.register

#다 만들었으면 유저 생성하기: python manage.py createsuperuser
#이름: admin 이메일: 그냥 넘어감 pw: 1
#runserver해서 /admin 들어가기