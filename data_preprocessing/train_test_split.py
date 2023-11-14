from sklearn.model_selection import train_test_split
import os
import shutil

if __name__ == "__main__":
    # folder_path = 'e:\FPT University\Semester 9\AIP490\Data\Train\Humans'
    # train_folder = 'e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_train_HR'
    # test_folder = 'e:\FPT University\Semester 9\AIP490\Data\Train\Human_Faces\Human_Faces_test_HR'

    folder_path = 'e:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape\GTmod8'
    train_folder = 'e:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_train_HR\GTmod8'
    test_folder = 'e:\FPT University\Semester 9\AIP490\Data\Train\Vietnamese_Landscape_test_HR\GTmod8'

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    image_names = os.listdir(folder_path)
    train_names, test_names = train_test_split(image_names, test_size=0.1, random_state=42)

    print(f'Training set: {len(train_names)} images')
    print(f'Test set: {len(test_names)} images')

    for name in train_names:
        shutil.copy(os.path.join(folder_path, name), os.path.join(train_folder, name))
    for name in test_names:
        shutil.copy(os.path.join(folder_path, name), os.path.join(test_folder, name))