from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
from glob import glob
import numpy as np

if __name__ == '__main__':
    fe = FeatureExtractor()

    # Iterate through images (Change the path based on your image location)
    for path in glob(r"c:\\Self_Study\\HappyVirus\\최종(웹)\\web\\myapp\\static\\img\\*"):
        for img_path in Path(path).glob("*.jpg"):
            print(img_path)

            # feature extration
            feature = fe.extract(img=Image.open(img_path))

            # Save the Numpy array (.npy) on designated path
            feature_path = Path(path) / (img_path.stem + ".npy")  
            print(feature_path)

            np.save(feature_path, feature)
            #C:/Users/user/Desktop/프로젝트/HappyVirus/최종(웹)/web/myapp/offline.py
