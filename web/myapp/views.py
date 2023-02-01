from django.shortcuts import render #함수를 실행하면 html이 실행됨
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User #입력받은 회원정보로 회원가입을 하기 위해서 import 시켜줌
from django.contrib.auth.hashers import check_password #비밀번호 변경하기 위해서 import 시켜줌 



def index(request):
    return render(request, 'index.html')


def register(request):   #회원가입 페이지를 보여주기 위한 함수
    
    #입력값 받아오기
    if request.method == "POST":
        print(request.POST)
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        nickname = request.POST["nickname"]
        email = request.POST["email"]
        
        if password1 == password2:
        
            #고정형식
            user = User.objects.create_user(username, email, password1)
            
            #추가정보
            #user.password2 = password2
            user.fullname = fullname
            user.nickname = nickname
            
            #저장
            user.save()
            
            #회원가입 끝나면 로그인 창으로 이동
            return redirect("login")
        
            #바로 로그인된 상태로 만들어주고 싶으면 
            #login(request, user)

    return render(request, 'join.html') 

def login_view(request):   #로그인 페이지를 보여주기 위한 함수

    if request.method=="POST":
        #변수username에 username 담아주기 
        username = request.POST['username']
        #변수password에 password 담아주기 
        password = request.POST['password']

        #받은 id와 pw 값이 일치하지 않으면 none값을 줌
        user = authenticate(username=username, password=password)
        if user is not None:
            print("로그인 성공")
            login(request, user)
            
            #로그인 끝나면 index 창으로 이동
            return redirect("index")
            
        else:
            print("로그인 실패")

    return render(request, 'login.html') 

def logout_view(request):   #로그아웃 페이지를 보여주기 위한 함수
    logout(request)
    return redirect("index")

def modify_view(request): #내 정보 수정 페이지를 보여주기 위한 함수
    if request.method == 'GET':
        return render(request, 'mypage.html')

    elif request.method == 'POST':
        user = request.user

        fullname= request.POST.get('fullname')
        email = request.POST.get('email')
        nickname =request.POST.get('nickname')

    
        user.fullname = fullname
        user.email = email
        user.nickname = nickname

        user.save()

        #바로 로그인된 상태로 만들어주고 싶으면 
        login(request, user)
        #회원가입 끝나면 로그인 창으로 이동
        return redirect("mypage")

    return render(request, 'mypage.html') 


def change_pw_view(request):
    if request.method == 'GET':
        return render(request, 'change_pw.html')


    elif request.method == 'POST':
        user = request.user

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 == password2:       
            user.set_password(password1)
            user.save()

            #바로 로그인된 상태로 만들어주고 싶으면 
            login(request, user)

            #회원가입 끝나면 로그인 창으로 이동
            return redirect("mypage")

    return render(request, 'change_pw.html') 

def delete_view(request): #탈퇴하기 적용
    request.user.delete()
    return redirect('index')


def service(request):   #서비스 페이지를 보여주기 위한 함수
    return render(request, 'service.html') 

def contact(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'contact.html') 

def mypage(request):   #마이페이지를 보여주기 위한 함수
    return render(request, 'mypage.html') 

def upload(request):   #업로드페이지를 보여주기 위한 함수
    return render(request, 'upload.html') 

def collection(request):   #컬렉션페이지를 보여주기 위한 함수
    return render(request, 'collection.html') 

def upload_list(request):   #업로드현황을 보여주기 위한 함수
    return render(request, 'upload_list.html') 
