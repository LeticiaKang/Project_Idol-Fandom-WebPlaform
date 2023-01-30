from django.db import models

# Create your models here.
# class 테이블명(models.Model):

#             컬럼정의

#             ( 필드명 = models.fieldType메소드(옵션) )
class Info(models.Model):
    no = models.AutoField(primary_key=True)
    user_name=models.CharField(min_length=2)
    user_id=models.CharField(min_length=3)
    user_pw=models.CharField(min_length=8)