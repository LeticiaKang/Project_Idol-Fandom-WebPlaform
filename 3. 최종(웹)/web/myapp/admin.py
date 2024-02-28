from django.contrib import admin

#현재 같은 디렉토리에서 models안에 있는 User 불러오기
from .models import User
# Register your models here.

#만든 User모델을 등록하기
admin.site.register(User)

