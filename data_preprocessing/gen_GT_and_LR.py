import os
import random
from PIL import Image

def gen_GT_and_LR(image_HR_dir, saved_HR_dir, saved_LR_dir, scale):
    """
        image_HR_dir: Đường dẫn thư mục chứa bộ data High Resolution
        saved_HR_dir: Đường dẫn thư mục để lưu data High Resolution mod
        saved_LR_dir: Đường dẫn thư mục để lưu data Low Resolution
        scale: Tỷ lệ sinh ảnh Low Resolution
    """
    list_image_names = os.listdir(image_HR_dir)  # Lấy dir của toàn bộ tập ảnh
    total_image = len(list_image_names)   # Tổng số lượng ảnh trong tập ảnh

    if not os.path.exists(os.path.join(saved_HR_dir)):
        os.mkdir(os.path.join(saved_HR_dir))
    if not os.path.exists(os.path.join(saved_LR_dir)):
        os.makedirs(os.path.join(saved_LR_dir))

    for image_name in list_image_names:
        img = Image.open(os.path.join(image_HR_dir, image_name))
        width, height = img.size
        width -= width % scale
        height -= height % scale
        HR_image = img.crop((0, 0, width, height))
        HR_image.save(os.path.join(saved_HR_dir, image_name))
        print(image_name, "HR has been saved! Image size: ", HR_image.size)

        LR_image = HR_image.resize((width//scale, height//scale), resample=Image.BICUBIC)
        LR_image.save(os.path.join(saved_LR_dir, image_name))
        print(image_name, "LR has been saved! Image size: ", LR_image.size)

if __name__ == "__main__": 
    # gen_GT_and_LR(image_HR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\BSD100\original", 
    #               saved_HR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\BSD100\GTmod8", 
    #               saved_LR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\BSD100\LRbicx8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\Manga109\original", 
    #               saved_HR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\Manga109\GTmod8", 
    #               saved_LR_dir="e:\Coding\Python\Learning\AIP490\HAT\datasets\Manga109\LRbicx8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_HR/train", 
    #               saved_HR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_HR/GTmod8", 
    #               saved_LR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_LR/LRbicx8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_HR/test", 
    #               saved_HR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_HR/GTmod8", 
    #               saved_LR_dir="E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_LR/LRbicx8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/DIV2K-Mosaic/DIV2K_train_HR", 
    #               saved_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/DIV2K-Mosaic/DIV2K_train_HR_GTmod8", 
    #               saved_LR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/DIV2K-Mosaic/DIV2K_train_LR_bicubic/X8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set5/original", 
    #               saved_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set5/GTmod8", 
    #               saved_LR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set5/LRbicx8", 
    #               scale = 8)
    # gen_GT_and_LR(image_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set14/original", 
    #               saved_HR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set14/GTmod8", 
    #               saved_LR_dir=r"/fpt/thinhnd/AI-Capstone/HAT-experiment/datasets/Set14/LRbicx8", 
    #               scale = 8)


    pass