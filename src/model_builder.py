import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras import layers, Model

IMG_SIZE = 224

def build_model(num_classes):
    base = EfficientNetB3(
        weights="imagenet",
        include_top=False,
        input_shape=(IMG_SIZE, IMG_SIZE, 3)
    )

    base.trainable = False  # freeze giai đoạn 1

    x = layers.GlobalAveragePooling2D()(base.output)
    x = layers.Dropout(0.3)(x)
    output = layers.Dense(num_classes, activation="softmax")(x)

    model = Model(base.input, output)
    return model

