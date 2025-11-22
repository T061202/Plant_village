import os
from PIL import Image

# ĐƯỜNG DẪN DATASET CỦA BẠN
DATASET_DIR = "D:/Plant_village/data"

def is_image_broken(path):
    try:
        img = Image.open(path)
        img.verify()
        return False
    except Exception:
        return True

def scan_and_clean(folder):
    deleted = 0
    total = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            total += 1
            file_path = os.path.join(root, file)

            if is_image_broken(file_path):
                print("❌ Ảnh lỗi:", file_path)
                os.remove(file_path)
                deleted += 1

    print("\n============================")
    print(f"Tổng số ảnh kiểm tra: {total}")
    print(f"Số ảnh bị lỗi đã xóa: {deleted}")
    print("============================")

if __name__ == "__main__":
    scan_and_clean(DATASET_DIR)
