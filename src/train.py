import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras import layers, models

# =============================
# CONFIG
# =============================
BASE_DIR = "D:/Plant_village"
DATASET_DIR = os.path.join(BASE_DIR, "Data/train")
MODEL_DIR = os.path.join(BASE_DIR, "model")

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS_STAGE1 = 10
EPOCHS_STAGE2 = 10


# =============================
# BUILD MODEL
# =============================
def build_model(num_classes):
    base = EfficientNetB3(
        include_top=False,
        weights="imagenet",
        input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)
    )

    base.trainable = False  # freeze stage 1

    x = layers.GlobalAveragePooling2D()(base.output)
    x = layers.Dropout(0.3)(x)
    output = layers.Dense(num_classes, activation="softmax")(x)

    model = models.Model(inputs=base.input, outputs=output)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-3),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model, base


# =============================
# LOAD DATASET
# =============================
train_gen = ImageDataGenerator(
    rescale=1/255.0,
    validation_split=0.1
)

train_ds = train_gen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True
)

val_ds = train_gen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)

num_classes = train_ds.num_classes
print(f"Số lớp: {num_classes}")


# =============================
# TRAIN STAGE 1
# =============================
model, base_model = build_model(num_classes)

print("\n===== TRAINING STAGE 1 (freeze base) =====")
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_STAGE1
)


# =============================
# TRAIN STAGE 2 – UNFREEZE
# =============================
print("\n===== TRAINING STAGE 2 (unfreeze base) =====")

base_model.trainable = True

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-4),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_STAGE2
)


# =============================
# SAVE MODEL (TensorFlow SavedModel)
# =============================
os.makedirs(MODEL_DIR, exist_ok=True)

print("\n💾 Đang lưu model dạng TensorFlow SavedModel (ổn định nhất)…")

# ❗ KHÔNG DÙNG model.save() – sẽ lỗi JSON
# ❗ KHÔNG DÙNG model.export() – sẽ lỗi ReplicaContext
tf.saved_model.save(model, MODEL_DIR)

print("🎉 TRAINING DONE – MODEL ĐÃ LƯU TẠI:", MODEL_DIR)
