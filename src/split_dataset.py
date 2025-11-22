import os
import shutil
import random

RAW_DIR = "data/raw/"
BASE_DIR = "data/"

TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "val")
TEST_DIR = os.path.join(BASE_DIR, "test")

SPLIT_TRAIN = 0.8
SPLIT_VAL = 0.1
SPLIT_TEST = 0.1

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_data():
    classes = os.listdir(RAW_DIR)
    
    for cls in classes:
        raw_class_dir = os.path.join(RAW_DIR, cls)

        if not os.path.isdir(raw_class_dir):
            continue

        # Tạo thư mục class cho train/val/test
        create_dir(os.path.join(TRAIN_DIR, cls))
        create_dir(os.path.join(VAL_DIR, cls))
        create_dir(os.path.join(TEST_DIR, cls))

        images = os.listdir(raw_class_dir)
        random.shuffle(images)

        total = len(images)
        train_end = int(total * SPLIT_TRAIN)
        val_end = train_end + int(total * SPLIT_VAL)

        train_files = images[:train_end]
        val_files = images[train_end:val_end]
        test_files = images[val_end:]

        # Copy ảnh
        for f in train_files:
            shutil.copy(os.path.join(raw_class_dir, f),
                        os.path.join(TRAIN_DIR, cls))

        for f in val_files:
            shutil.copy(os.path.join(raw_class_dir, f),
                        os.path.join(VAL_DIR, cls))

        for f in test_files:
            shutil.copy(os.path.join(raw_class_dir, f),
                        os.path.join(TEST_DIR, cls))

        print(f"[OK] {cls} — Train: {len(train_files)}, Val: {len(val_files)}, Test: {len(test_files)}")

    print("\n🎉 DONE! Dataset split successfully.")

if __name__ == "__main__":
    split_data()
