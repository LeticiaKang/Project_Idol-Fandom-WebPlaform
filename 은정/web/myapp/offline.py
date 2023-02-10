from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    fe = FeatureExtractor()

    # Iterate through images (Change the path based on your image location)
    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        
        # feature extration
        feature = fe.extract(img=Image.open(img_path))
        
        # Save the Numpy array (.npy) on designated path
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        print(feature_path)
        
        np.save(feature_path, feature)
