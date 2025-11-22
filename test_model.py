import tensorflow as tf

# Đường dẫn model đã lưu
MODEL_DIR = "model"

# Load lại model
model = tf.keras.models.load_model(MODEL_DIR)

# In kiến trúc model
model.summary()

print("Model loaded successfully!")
