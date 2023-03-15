import tensorflow.keras.models
from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.xception import Xception, preprocess_input
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
from tensorflow.keras.models import Model
import numpy as np

# See https://keras.io/api/applications/ for details

class FeatureExtractor:
    def __init__(self):
        
        # Use model as the architecture and ImageNet for the weight
        # base_model = InceptionResNetV2(weights='imagenet') # 이미지넷의 학습 카테고리는 무엇인지, 어떤 가중치를 사용했는지
        # MODEL_PATH = './static/model/InceprionResnetV2_epoch_9_batch_32.h5'
        self.model = tensorflow.keras.models.load_model("C:\Self_Study\HappyVirus\최종(웹)\web\myapp\static\model\InceprionResnetV2_epoch_9_batch_32.h5")

    def extract(self, img):
        # 모델에 맞게 input할 image의 크기를 resizing한다.
        img = img.resize((299, 299))
        
        # Convert the image color space
        img = img.convert('RGB')  # Make sure img is color
        
        # Reformat the image
        x = image.img_to_array(img)  # To np.array. Height x Width x Channel. dtype=float32
        x = np.expand_dims(x, axis=0)  # (H, W, C)->(1, H, W, C), where the first elem is the number of img
        x = preprocess_input(x)  # Subtracting avg values for each pixel
        
        # Extract Features
        feature = self.model.predict(x)[0]  # (1, 4096) -> (4096, )
        return feature / np.linalg.norm(feature)  # Normalize

