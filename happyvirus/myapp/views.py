from django.shortcuts import render #함수를 실행하면 html이 실행됨
from django.contrib.auth import authenticate, login
# #로그인, 로그아웃 기능 사용하기 위해
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import auth

def index(request):
    return render(request, 'index.html')


def register(request):   #회원가입 페이지를 보여주기 위한 함수
    return render(request, 'join.html') #register를 요청받으면 register.html 로 응답.

def login(request):   #로그인 페이지를 보여주기 위한 함수

    if request.method=="POST":
        #변수user_id에 user_id 담아주기 
        user_id = request.POST['user_id']
        #변수userpw에 user_id 담아주기 
        user_pw = request.POST['user_pw']

        #받은 id와 pw 값이 일치하지 않으면 none값을 줌
        user = authenticate(user_id=user_id, user_pw=user_pw)
        if user is not None:
            print("로그인 성공")
            login(request, user)
        else:
            print("로그인 실패")
    return render(request, 'login.html') #register를 요청받으면 register.html 로 응답.




def service(request):   #서비스 페이지를 보여주기 위한 함수
    return render(request, 'service.html') #register를 요청받으면 register.html 로 응답.

def contact(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'contact.html') #register를 요청받으면 register.html 로 응답.

def mypage(request):   #마이페이지를 보여주기 위한 함수
    return render(request, 'mypage.html') #register를 요청받으면 register.html 로 응답.

def upload(request):   #업로드페이지를 보여주기 위한 함수
    return render(request, 'upload.html') #register를 요청받으면 register.html 로 응답.

def collection(request):   #컬렉션페이지를 보여주기 위한 함수
    return render(request, 'collection.html') #register를 요청받으면 register.html 로 응답.

def upload_list(request):   #업로드현황을 보여주기 위한 함수
    return render(request, 'upload_list.html') #register를 요청받으면 register.html 로 응답.

