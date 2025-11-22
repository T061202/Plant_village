import numpy as np
from tensorflow.keras.preprocessing import image

IMG_SIZE = (224, 224)

def load_and_preprocess(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img
