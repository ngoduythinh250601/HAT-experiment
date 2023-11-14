import os

def naming(folder_path):
    list_files = os.listdir(folder_path)
    for i, file_name in enumerate(list_files, start=1):
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, f'{i:04}.png')  # Đặt định dạng tên mới tùy thuộc vào loại tệp của bạn
        print(new_path)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    # naming(r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR\GTmod8")
    # naming(r"e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR\GTmod8")

    pass