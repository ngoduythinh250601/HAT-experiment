from torchvision import transforms
import os
import random
from PIL import Image
import matplotlib.pyplot as plt

def gen_GT(image_HR_dir, saved_HR_dir, scale):
    """
        image_HR_dir: Đường dẫn thư mục chứa bộ data High Resolution
        saved_HR_dir: Đường dẫn thư mục để lưu data High Resolution mod
        scale: Tỷ lệ sinh ảnh Low Resolution
    """
    list_image_names = os.listdir(image_HR_dir)  # Lấy dir của toàn bộ tập ảnh
    total_image = len(list_image_names)   # Tổng số lượng ảnh trong tập ảnh

    if not os.path.exists(os.path.join(saved_HR_dir)):
        os.makedirs(os.path.join(saved_HR_dir))

    for image_name in list_image_names:
        img = Image.open(os.path.join(image_HR_dir, image_name))
        width, height = img.size
        width -= width % scale
        height -= height % scale
        HR_image = img.crop((0, 0, width, height))
        HR_image.save(os.path.join(saved_HR_dir, image_name))
        print(image_name, "HR has been saved! Image size: ", HR_image.size)


if __name__ == "__main__": 
    # gen_GT(image_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR\original", 
    #               saved_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR\GTmod8", 
    #               scale = 8)
    # gen_GT(image_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR\original", 
    #               saved_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR\GTmod8", 
    #               scale = 8)

    gen_GT(image_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\500", 
                    saved_HR_dir=r"e:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape\GTmod8", 
                    scale = 8)
    

    pass