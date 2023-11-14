import os
from PIL import Image
import random

def convert_to_gray_scale(image_path):
    img = Image.open(image_path)
    gray_img = img.convert('L')
    gray_img.save(image_path)
    print(f"{image_path} converted!")

if __name__ == "__main__":
    folder_path = r"e:\FPT University\Semester 9\AIP490\Data\Train\Humans"
    image_names = os.listdir(folder_path)

    # Lặp qua 50% số lượng ảnh và chuyển thành ảnh xám
    for image_name in random.sample(image_names, int(0.5 * len(image_names))):
        image_path = os.path.join(folder_path, image_name)
        convert_to_gray_scale(image_path)
        