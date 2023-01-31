from django.shortcuts import render #함수를 실행하면 html이 실행됨

# def print_test(request):
#     return HttpResponse("출력 완료!")
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def register(request):   #회원가입 페이지를 보여주기 위한 함수
    return render(request, 'join.html') #register를 요청받으면 register.html 로 응답.

def login(request):   #로그인 페이지를 보여주기 위한 함수
    return render(request, 'login.html') #register를 요청받으면 register.html 로 응답.

def service(request):   #서비스 페이지를 보여주기 위한 함수
    return render(request, 'service.html') #register를 요청받으면 register.html 로 응답.

def contact(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'contact.html') #register를 요청받으면 register.html 로 응답.

def mypage(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'mypage.html') #register를 요청받으면 register.html 로 응답.

def upload(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'upload.html') #register를 요청받으면 register.html 로 응답.

def collection(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'collection.html') #register를 요청받으면 register.html 로 응답.

def upload_list(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'upload_list.html') #register를 요청받으면 register.html 로 응답.
