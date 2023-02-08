import numpy as np
from glob import glob
from PIL import Image as pil_img
from myapp.feature_extractor import FeatureExtractor

class Algorithm:
    def __init__(self, file):
        self.name = file

    def UploadFileFeature(self):
        """
            이미 저장되어 있는 npy파일의 feature와 경로를 가져오기 위한 함수임.
            input : 없음, return features, img_paths
        """
        features, img_paths = [], []
        # 1. 추출한 feature npy파일을 모두 가져와서 객체로 for문 돌리기
        count = 0
        for feature_path in glob(r"C:\Self_Study\web\myapp\static\feature\*.npy"):
            img_paths.append(feature_path)

            print(count, "★★★★★★★", features)
            print(count, "★★★★★★★", type(features))
            print(count, "★★★★★★★",type(np.load(feature_path).tolist()))

            features = np.append(features, np.load(feature_path), axis=0)  # 해당 파일의 경로에 저장된 npy(array)파일을 features 저장
            count+=1
        return features, img_paths # array로 바꿔서


    # print("2-1. ★★★ === Image.objects.lastest('image') ====", Image.objects.last())
    # print("2-2. ★★★ === Image.objects.lastest('image') ====", type(Image.objects.last()))
    # print("2-4", type(request.FILES.get("image").file))
    # img = Image.open(Path("web/image/%y/%m/%d")/(str(form.files["image"])))
    # img = pil_img.open(io.BytesIO(Image.objects.last()).read())
    # 2. 유사 사진 찾기
    def FindSimilarPicture(self):
        """
            UploadFileFeature에서 받아온 features, img_paths과
            업로드된 파일의 feature를 추출하여 경로를 계산해 제일 가까운 30개를 return함
            input : request.FILES.get("image").file, return [(dists[id], img_paths[id]) for id in ids]
        """
        features, img_paths = self.UploadFileFeature()
        print("★★★★★★★",features)
        scores= []
        img = pil_img.open(self.file)
        query = FeatureExtractor.extract(img)
        print("3. myapp.view =========== 이미지 특성 추출 성공! ===========")
        # print("3-1. ===== query ======", query.shape)
        # print("3-1. ===== query.type ======", type(query))
        # print("3-2. ◆◆◆◆ features.shpae ======", features.shape)
        # print("3-3. ◆◆◆◆ features.type ======", type(features))
        # print("3-4. ◆◆◆◆ featurese ======", features)

        dists = np.linalg.norm(features - query, axis=1)   # 업로드 사진과 데이터간 거리(L2 distances) 측정/저장

        ids = np.argsort(dists)[:30]  # np.argsort는 배열안의 숫자를 오름차순해서 인덱스로 표현 해준다. 상위 30개만 ids에 다시 저장
        scores = [(dists[id], img_paths[id]) for id in ids]    # 그래서 for문으로 dists[id]에 넣으면 인덱스 역할을 해서 순서대로 뽑힘.

        return scores