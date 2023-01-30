from django.shortcuts import render #함수를 실행하면 html이 실행됨

# def print_test(request):
#     return HttpResponse("출력 완료!")
def main(request):
    return render(request, 'index.html')

def register(request):   #회원가입 페이지를 보여주기 위한 함수
    return render(request, 'join.html') #register를 요청받으면 register.html 로 응답.
