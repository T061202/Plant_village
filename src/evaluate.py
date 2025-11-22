import tensorflow as tf
from dataset import create_generators

TEST_DIR = "data/test/"
MODEL_PATH = "model/model.h5"

model = tf.keras.models.load_model(MODEL_PATH, compile=False)

_, val_gen = create_generators("data/train/", "data/val/")

loss, acc = model.evaluate(val_gen)
print(f"Validation accuracy: {acc*100:.2f}%")
