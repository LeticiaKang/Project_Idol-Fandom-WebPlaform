from django.db import models
#AbstractUser: 장고에서 제공하는 로그인 기능 사용하기 위한 모델
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


#AbstractUser 상속: 장고에서 제공하는 유저에 관련된 모든 기능을 사용할 수 있게 됨
class User(AbstractUser):
    nickname=models.CharField(max_length=10)
    fullname=models.CharField(max_length=20)
    

# 이미지 저장을 위한 모델
class Image(models.Model):
    image=models.ImageField(upload_to="img/%y/%m/%d")

    # AbstractUser 상속: 장고에서 제공하는 유저에 관련된 모든 기능을 사용할 수 있게 됨

    # pass


class Posting(models.Model):
    content = models.TextField()
    # icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # pip install pillow / 폴더: upload_to="img/%y"

    created_at = models.DateTimeField(auto_now_add=True)  # 추가될때만!! add될때 한번 저장되고 끝남
    updated_at = models.DateTimeField(auto_now=True)  # 수정, save할 때 마다 True

    class Meta():  # ordering이 정보에 대한 내용이구나 라는걸 알려줘야됨.
        ordering = ['-created_at', ]  # created_at 을 descending(내림차순)으로.

    # detail.html page가 있으면(쓸거라면) 이걸 만들어줘야됨
    def get_absolute_url(self):
        return reverse("posting_detail", kwargs={"posting_id": self.pk})

    def __str__(self):
        return f'{self.pk}: {self.content[:10]}'
    

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    # comments_set을 대신하겠다는게 related_name. 대신 .all()까진 써야됨. posting.comment_set과 같은 말
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['created_at', ]
    
    def __str__(self):
        return f'{self.id}: {self.content[:10]}'


