from django.contrib import admin
from.models import User

@admin.register(User) #가져온 모델을 admin페이지에 등록
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm',
    )