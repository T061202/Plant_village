import json
import tensorflow as tf
from helpers import load_and_preprocess

LABEL_FILE = "D:/Plant_village/labels.json"
MODEL_PATH = "D:/Plant_village/model"

# Load labels
with open(LABEL_FILE, "r") as f:
    LABELS = json.load(f)

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(img_path):
    img = load_and_preprocess(img_path)
    preds = model.predict(img)[0]
    idx = preds.argmax()
    return {
        "label": LABELS[idx],
        "confidence": float(preds[idx])
    }
