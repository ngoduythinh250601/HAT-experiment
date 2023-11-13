from load_models import Model
import cv2


if __name__ == '__main__':
    models = Model("E:\HAT-main\deploy\options\HAT-S_SRx4.yml")
    img = cv2.imread("E:\HAT-main\deploy\images\wave alpha.jpg", cv2.IMREAD_COLOR).astype(float) / 255
    sr_img = models.process(img)

    # Hiển thị hình ảnh
    cv2.imshow("Image", sr_img)
    cv2.waitKey(0)