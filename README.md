# 좋아하는 아이돌의 사진을 찾아주는 팬덤 플랫폼(ByFan)
## 프로젝트 목표
- 아이돌 팬들을 위한 웹 플랫폼으로, 사용자가 선호하는 아이돌 사진을 입력하면 DB에서 이와 비슷한 사진을 추천해준다.(핀터레스트와 같은 기능을 구현하고자 했다)

## 요구사항(주요 기능)
- 회원가입, 로그인, 사진 검색 서비스, 소통공간으로 구성되어 있다.
- **회원가입** : 각 필드에 맞는 형식을 검증
- **로그인** : DB에 저장한 데이터로 로그인
- **사진 검색 서비스** : DL로 구현한 알고리즘 모델을 적용하여, 사진 유사도를 기반으로 비슷한 사진을 보여준다.
  - 사용자가 사진을 제출하는 페이지
  - 결과 반환 페이지
- **소통 공간** : 사용자가 원하는 사진을 게시글로 올리고, 댓글을 작성할 수 있다.
  - 게시글 및 댓글 생성, 수정, 삭제

## 담당 업무
- **Django REST Framework를 이용하여 백엔드를 구축**
- **MySQL을 이용해 DB 구축, ORM을 이용하여 DB 생성 및 맵핑**
  - User : 사용자 정보
  - Image : 이미지 데이터 저장
  - Posting : 게시글
  - Comment : 댓글
- **인증**
  - AbstractUser 상속을 통한 인증 시스템 구축
- **DL모델 구축**
  - SSD, Inception, InceptionResnet 등 CNN 기반의 다양한 모델을 학습시켜 비교
  - 비교 : EfficientnetV2s, InceptionResnetV2, InceptionV3, Resnet50, SSD, VGG19, yoloV5
      - 최종적으로 InceptionResnetV2를 이용하여 정확도 85%로 구현 완료
  - 알고리즘 구축 내용 정리 : https://github.com/LeticiaKang/DL_Image-Classification
- **웹과 DL모델 연결**
  - 프로젝트와 DL모델 core를 합하여 연결 

## 개발환경
- 프론트엔드
  - HTML, CSS, Bootstrap, JS
- 백엔드
  - Python, Django REST Framework
  - Python Imaging Library(PIL) : 이미지 처리
- DB
  - MySQL
- 알고리즘 모델 개발
  - Tensorflow, Keras

## 구현 이미지
| 회원가입 | 로그인 페이지 |
| --- | --- |
| ![회원가입](https://github.com/LeticiaKang/Project_board/assets/87592790/37ff022e-4257-4678-9e18-04a7d0d43544) | ![로그인 페이지](https://github.com/LeticiaKang/Project_board/assets/87592790/f46ab0ac-188d-4f81-8a8d-c717d6ed9089) |

| **사진 업로드** | **업로드 후 검색결과** |
| --- | --- | 
| ![사진 업로드](https://github.com/LeticiaKang/Project_board/assets/87592790/e4397499-7832-4830-8279-ec18214d77a1) | ![업로드 후 검색결과](https://github.com/LeticiaKang/Project_board/assets/87592790/2eb0f89a-e61d-42d5-89c3-845fcbf77215) | 

| 게시글 | 댓글 |
| --- | --- |
|![image](https://github.com/LeticiaKang/Project_board/assets/87592790/ffb778b2-cfb0-4f2e-a77c-628cf4ab2340)|![image](https://github.com/LeticiaKang/Project_board/assets/87592790/b90e6e80-857c-49bf-9c85-21902dad112e)|

| 메인페이지1 | 메인페이지2 |
| --- | --- |
| ![메인페이지1](https://github.com/LeticiaKang/Project_board/assets/87592790/e0415a77-8e04-40a7-869b-cedb819c93bd) | ![메인페이지2](https://github.com/LeticiaKang/Project_board/assets/87592790/cb2a2a81-7ace-421d-890a-a2f7e8e24c6a) |

| 메인페이지3 | CS 문의 |
| --- | --- |
| ![메인페이지3](https://github.com/LeticiaKang/Project_board/assets/87592790/f1a1e165-fd25-46ca-97f8-d11dcf360c22) | ![CS 문의](https://github.com/LeticiaKang/Project_board/assets/87592790/4ec1c7c4-bbca-4dbd-810d-ea346e2a6895) |
