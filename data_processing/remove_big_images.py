import os
from PIL import Image

def delete_file(file_path):
    # Kiểm tra xem tệp có tồn tại không trước khi xóa
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Tệp {file_path} đã bị xóa.')
    else:
        print(f'Tệp {file_path} không tồn tại.')

def filter_images_by_size(checking_dir, dependent_dirs, max_width, max_height):
    """
        checking_dir: Đường dẫn thư mục chứa bộ data High Resolution
        dependent_dirs: Các đường dẫn thư mục chứa bộ data Low Resolution
    """
    for filename in os.listdir(checking_dir):
        image_path = os.path.join(checking_dir, filename)
        with Image.open(image_path) as img:
            width, height = img.size
            if width > max_width and height > max_height:
                delete_file(image_path)
                for image_LR_dir in dependent_dirs:
                    delete_file(os.path.join(image_LR_dir, filename))
                print(f"{filename} ({img.size}) removed")
        

if __name__ == "__main__": 
    # filter_images_by_size(checking_dir="datasets/Human_Faces/Human_Faces_test_HR/GTmod8", 
    #                       dependent_dirs=["datasets/Human_Faces/Human_Faces_test_LR_deep_blind/X4", "datasets/Human_Faces/Human_Faces_test_LR_deep_blind/X8"], 
    #                       max_width=2048, 
    #                       max_height=2048)

    pass