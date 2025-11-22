import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 224
BATCH_SIZE = 32

def create_generators(train_dir, val_dir):
    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        zoom_range=0.2,
        shear_range=0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )

    val_gen = ImageDataGenerator(rescale=1./255)

    train_ds = train_gen.flow_from_directory(
        train_dir,
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode="categorical"
    )

    val_ds = val_gen.flow_from_directory(
        val_dir,
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        class_mode="categorical"
    )

    return train_ds, val_ds
