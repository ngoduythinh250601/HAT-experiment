from PIL import Image
from os.path import join


def merge_4_images(folder_dir, image_names, saved_name):
    image1 = Image.open(join(folder_dir, image_names[0]))
    image2 = Image.open(join(folder_dir, image_names[1]))
    image3 = Image.open(join(folder_dir, image_names[2]))
    image4 = Image.open(join(folder_dir, image_names[3]))

    width, height = image1.size
    image2 = image2.resize((width, height))
    image3 = image3.resize((width, height))
    image4 = image4.resize((width, height))

    result_image = Image.new("RGB", (2 * width, 2 * height))
    result_image.paste(image1, (0, 0))
    result_image.paste(image2, (width, 0))
    result_image.paste(image3, (0, height))
    result_image.paste(image4, (width, height))

    result_image.save(join(folder_dir, f"{saved_name}.png"))


def merge_list_of_images(folder_dir, image_names, saved_name):
    spacing = 10
    images = [Image.open(join(folder_dir, filename)) for filename in image_names]

    width = sum(img.width for img in images) + (len(images) - 1) * spacing
    height = max(img.height for img in images)

    result_image = Image.new("RGB", (width, height), (255, 255, 255))
    x_offset = 0
    for img in images:
        result_image.paste(img, (x_offset, 0))
        x_offset += img.width + spacing

    result_image.save(join(folder_dir, saved_name))


if __name__ == "__main__":
    # merge_4_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Bar chart\Upscale x4\PSNR",
    #     image_names=["set_5.png", "set14.png", "BSD100.png", "Manga109.png"],
    #     saved_name="merged.png",
    # )
    # merge_4_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Bar chart\Upscale x4\SSIM",
    #     image_names=["Set5.png", "Set14.png", "BSD100.png", "Manga109.png"],
    #     saved_name="merged.png",
    # )
    # merge_4_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Bar chart\Upscale x8\PSNR",
    #     image_names=["Set5.png", "Set14.png", "BSD100.png", "Manga109.png"],
    #     saved_name="merged.png",
    # )
    # merge_4_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Bar chart\Upscale x8\SSIM",
    #     image_names=["Set5.png", "Set14.png", "BSD100.png", "Manga109.png"],
    #     saved_name="merged.png",
    # )

    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\main task x4",
    #     image_names=[
    #         "comic_LR.png",
    #         "comic_HAT-S_SRx4_from_scratch.png",
    #         "comic_HAT-S_SRx4_Patch-Mosaic.png",
    #         "comic_HAT-S_SRx4_PerceptualLoss_conv2_2.png",
    #         "comic_HAT-S_SRx4_MixLosses.png",
    #         "comic_GT.png",
    #     ],
    #     saved_name="merged.png",
    # )
    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\main task x8",
    #     image_names=[
    #         "comic_LR.png",
    #         "comic_HAT-S_SRx8_from_scratch.png",
    #         "comic_HAT-S_SRx8_Patch-Mosaic.png",
    #         "comic_HAT-S_SRx8_PerceptualLoss_conv2_2.png",
    #         "comic_HAT-S_SRx8_MixLosses.png",
    #         "comic_GT.png",
    #     ],
    #     saved_name="merged.png",
    # )
    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\additional task x4",
    #     image_names=[
    #         "0032_LR.png",
    #         "0032_HAT-S_SRx4_denoise_HumanFaces.png",
    #         "0032_GT.png",
    #     ],
    #     saved_name="merged1.png",
    # )
    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\additional task x4",
    #     image_names=[
    #         "0074_LR.png",
    #         "0074_HAT-S_SRx4_for_VietnamLandscape.png",
    #         "0074_GT.png",
    #     ],
    #     saved_name="merged2.png",
    # )
    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\additional task x8",
    #     image_names=[
    #         "0032_LR.png",
    #         "0032_HAT-S_SRx8_denoise_HumanFaces.png",
    #         "0032_GT.png",
    #     ],
    #     saved_name="merged1.png",
    # )
    # merge_list_of_images(
    #     folder_dir=r"e:\FPT University\Semester 9\AIP490\Reports\Final Report\Figures\Output Visualization\additional task x8",
    #     image_names=[
    #         "0074_LR.png",
    #         "0074_HAT-S_SRx8_for_VietnamLandscape.png",
    #         "0074_GT.png",
    #     ],
    #     saved_name="merged2.png",
    # )

    pass
