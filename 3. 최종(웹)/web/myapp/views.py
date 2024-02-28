from django.shortcuts import render, redirect, get_object_or_404 #함수를 실행하면 html이 실행됨
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User #입력받은 회원정보로 회원가입을 하기 위해서 import 시켜줌

from django.contrib.auth.hashers import check_password #비밀번호 변경하기 위해서 import 시켜줌 
from django.views.decorators.http import require_GET, require_POST

from myapp.models import Image
from myapp.form import ImageUpload

import numpy as np
from myapp.Route import route
from glob import glob
from PIL import Image as pil_img
from myapp.feature_extractor import FeatureExtractor

from .models import Posting, Comment
from .form import PostingModelForm, CommentModelForm

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



def contact(request):   #연락 페이지를 보여주기 위한 함수
    return render(request, 'contact.html') 

def mypage(request):   #마이페이지를 보여주기 위한 함수
    return render(request, 'mypage.html') 

def upload(request):   #업로드현황을 보여주기 위한 함수
    return render(request, 'upload.html') 

def collection(request):   #컬렉션페이지를 보여주기 위한 함수
    return render(request, 'collection.html') 
    
def upload_list(request):   #업로드현황을 보여주기 위한 함수
    return render(request, 'upload_list.html')

# ================= 알고리즘 =====================
def service(request):   #서비스 페이지를 보여주기 위한 함수

    # 2. post로 받아올 때
    if request.method == 'POST':
        print("1. myapp.view =========== post ===========")
        form = ImageUpload(data=request.POST, files=request.FILES)
        # print("1-1. ★★★ === type(request.FILES) ===", type(request.FILES))
        # print("1-2. ★★★ === form.files() ====", form.files["image"])

        if form.is_valid():
            form.save()
            print("2. myapp.view =========== form저장 성공! ===========")
            # print(request.FILES.get("image").file) #<_io.BytesIO object at 0x00000200AE5B72C0>
                # print(type(request.FILES.get("image").file)) #<class '_io.BytesIO'>
            img = pil_img.open(request.FILES.get("image").file)
            name = str(request.FILES.get("image"))
            scores = FindSimilarPicture(img, name[0]) #여기서 broadcasting 오류 발생
            print("★★★ 164 scores  ★★★★", scores)
            upload_image_path = "uploaded/test/" + name
            return render(request, 'result.html', {"scores" : scores, "upload_image_path":upload_image_path})

    else:
        form = ImageUpload()
    img=Image.objects.all()
    return render(request,"service.html",{"img":img,"form":form})

def FindSimilarPicture(img, name:str):
    """
        UploadFileFeature에서 받아온 features, img_paths과
        업로드된 파일의 feature를 추출하여 경로를 계산해 제일 가까운 30개를 return함
        input : request.FILES.get("image").file, return [(dists[id], img_paths[id]) for id in ids]
    """
    fe = FeatureExtractor()
    features, img_paths = [], []
    # count = 1
    # 1. 추출한 feature npy파일을 모두 가져와서 객체로 for문 돌리기
    print("현재 경로", route())
    for feature_path in glob(rf"{route()}\static\feature\{name}\*.npy"):
        img_paths.append(feature_path.replace("feature", "img").replace("npy", "jpg"))
        # print(img_paths)
        # print(count, "★★★★★★★", feature_path)
        # print(count, "★★★★★★★", type(features))
        # print(count, "★★★★★★★",type(np.load(feature_path).tolist()))
        features.append(np.load(feature_path))
        # count+=1
    features = np.array(features)

# print("2-1. ★★★ === Image.objects.lastest('image') ====", Image.objects.last())
# print("2-2. ★★★ === Image.objects.lastest('image') ====", type(Image.objects.last()))
# print("2-4", type(request.FILES.get("image").file))
# img = Image.open(Path("web/image/%y/%m/%d")/(str(form.files["image"])))
# img = pil_img.open(io.BytesIO(Image.objects.last()).read())
# 2. 유사 사진 찾기
    scores= []
    query = fe.extract(img)
    print("3. myapp.view =========== 이미지 특성 추출 성공! ===========")
    # print("3-1. ===== query ======", query.shape)
    # print("3-1. ===== query.type ======", type(query))
    # print("3-2. ◆◆◆◆ features.shpae ======", features.shape)
    # print("3-3. ◆◆◆◆ features.type ======", type(features))
    # print("3-4. ◆◆◆◆ featurese ======", features)
    dists = np.linalg.norm(features - query, axis=1)   # 업로드 사진과 데이터간 거리(L2 distances) 측정/저장

    ids = np.argsort(dists)[:10]   # np.argsort는 배열안의 숫자를 오름차순해서 인덱스로 표현 해준다. 상위 10개만 ids에 다시 저장
    scores = [(dists[id] , img_paths[id]) for id in ids]   # 그래서 for문으로 dists[id]에 넣으면 인덱스 역할을 해서 순서대로 뽑힘.
    return scores



@require_GET
def feed(request):
    postings = Posting.objects.all()
    return render(request, 'feed.html', {
        'postings': postings,
    })





@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'posting_list.html', {
        'postings': postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name 때문
    return render(request, 'posting_detail.html', {
            'posting': posting,
            'comments': comments,
    })


@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 데이터와 파일을 검증하고 저장할 준비를 한겨
    if form.is_valid():  # 검증!
        posting = form.save()  # 저장 => Posting 객체를 return
        return redirect(posting_list)  # 성공하면 detail page
    else:
        return redirect('posting_list')  #실패하면 list page


@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('posting_list')


@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # 가져올때 model에 의해 content를 가져오게 돼있음.
    if form.is_valid():  # content값만 검증함
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 척 만 하고 Comment 객체를 return 한다.
        comment.posting_id = posting.id  # 그러고 나서 commnet_id값을 직접 넣어준다.
        # 이건 comment.posting = posting 하면 id가 알아서 들어가기 때문에 윗줄과 아예 똑같은 코드이다.
        comment.save()
    return redirect(posting)


@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id, posting_id=posting_id)
    comment.delete()
    return redirect(posting)