import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []

# 추출한 feature npy파일을 모두 가져와서 객체로 for문 돌리기
for feature_path in Path("web/myapp/static/feature").glob("*.npy"):
    # 해당 파일의 경로에 저장된 npy파일의 array를 불러와서 빈리스트 features에 넣기
    features.append(np.load(feature_path))
    # 해당 파일의 이름만 가져오고 앞, 뒤에 경로와 jp g붙이기 
    img_paths.append(Path("web/myapp/static/img") / (feature_path.stem + ".jpg"))
    print(img_paths)
# features라는 이중리스트는 2차원의 array로 바꾸기
features = np.array(features)

# 주소만 있을 때, get이나 post로 요청이 들어오면 실행
@app.route('/', methods=['GET', 'POST'])
def index():
    scores = []
    if request.method == 'POST':
        print("===========","post","===========")
        # 업로드된 이미지 파일이름 가져오기('test (5).jpg')
        file = request.files['query_img']
        print("29"*5, file)
        
        # 이미지 저장하기
        img = Image.open(file.stream)  # PIL image
        
        
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # feature간의 거리가 가장 가까운 사진 찾기
        # 업로든 된 사진의 feature를 가져온다. - query
        query = fe.extract(img)

        # 둘 사이의 차이를 계산하여 행 기준으로 정규화한다.
        # 사진과의 거리를 모두 빈 리스트에 담는다. - dists
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features

        # np.argsort는 배열안의 숫자를 오름차순해서 인덱스로 표현 해준다. 상위 30개만 ids에 다시 저장
        ids = np.argsort(dists)[:30]

        # dists가 오름차순으로 인덱스가 ids에 저장되어 있음.
        # 그래서 for문으로 dists[id]에 넣으면 인덱스 역할을 해서 순서대로 뽑힘.

        scores = [(dists[id], img_paths[id]) for id in ids ]

        # index.html에 scores랑 query_path를 보냄.
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=scores)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run("0.0.0.0")
