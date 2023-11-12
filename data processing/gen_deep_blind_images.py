import cv2
import degradation_bsrgan as db
import os
from PIL import Image

def gen_LR_deep_blind(image_HR_dir, image_LR_dir, scale=8):
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
        img = db.imread_uint(os.path.join(image_HR_dir, image_name), 3)
        img = db.uint2single(img)
        sf = scale
        img_lq, img_hq = db.degradation_bsrgan(img, sf=sf)
        db.imsave(db.single2uint(img_lq), os.path.join(image_LR_dir, image_name))

        print(image_name, "LR has been saved! Image size: ", img_lq.shape)


if __name__ == "__main__":
    # gen_LR_deep_blind(image_HR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR\GTmod8", 
    #                   image_LR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_LR_deep_blind\X4", 
    #                   scale=4)
    # gen_LR_deep_blind(image_HR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR\GTmod8", 
    #                   image_LR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_LR_deep_blind\X8", 
    #                   scale=8)
    gen_LR_deep_blind(image_HR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR\GTmod8", 
                      image_LR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_LR_deep_blind\X4", 
                      scale=4)
    gen_LR_deep_blind(image_HR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR\GTmod8", 
                      image_LR_dir = r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_LR_deep_blind\X8", 
                      scale=8)