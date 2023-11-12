import os
from PIL import Image

def gen_LR_bicubic(image_HR_dir, image_LR_dir, scale=8):
    """
        image_HR_dir: Đường dẫn thư mục chứa bộ data High Resolution
        image_LR_dir: Đường dẫn thư mục để lưu bộ data Low Resolution
        scale: Tỷ lệ sinh ảnh Low Resolution
    """
    if os.path.exists(os.path.join(image_LR_dir)):
        print("Thư mục my_dir đã tồn tại.")
    else:
        os.mkdir(os.path.join(image_LR_dir))
        print("Đã tạo thư mục my_dir.")
    list_image_names = os.listdir(image_HR_dir)  # Lấy dir của toàn bộ tập ảnh 
    for image_name in list_image_names:
        img = Image.open(os.path.join(image_HR_dir, image_name))
        width, heigh = img.size
        LR_image = img.resize((width//scale, heigh//scale), resample=Image.BICUBIC)
        file_name_saved = image_name
        LR_image.save(os.path.join(image_LR_dir, file_name_saved))
        print(file_name_saved, "LR has been saved! Image size: ", img.size, " -> ", LR_image.size, "divisible" if width%scale == 0 and heigh%scale == 0 else "not divisible")

gen_LR_bicubic(image_HR_dir = "E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_HR/GTmod8", 
               image_LR_dir = "E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_LR/LRbicx4", 
               scale=4)
# gen_LR_bicubic(image_HR_dir = "E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_HR/GTmod8", 
#                image_LR_dir = "E:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_LR/LRbicx4", 
#                scale=4)