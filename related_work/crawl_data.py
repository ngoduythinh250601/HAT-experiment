import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import os


def crawl_image_urls_from_a_page(pageTarget, min_width, saved_dir, image_name_state):
    print(pageTarget)
    try:
        # Disable SSL verification (not recommended for security reasons)
        page = requests.get(pageTarget, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")
        wrapper = soup.find("body")
        images = wrapper.find_all("img")
        for image in images:
            try:
                image_url = image.get("src")

                # Skip images with the 'data' scheme
                if image_url.startswith("data:"):
                    continue

                if ".svg" in image_url:
                    continue

                response = requests.get(image_url)
                image = Image.open(io.BytesIO(response.content))
                width, height = image.size
                if width < min_width:
                    continue

                index = image_url.find("?")
                if index != -1:
                    image_url = image_url[:index]
                print(image_url, image.size)

                # Save the image to the folder (target is 1000 images -> name the image with 4 digits)
                image_name_state += 1
                image.save(os.path.join(saved_dir, f"{image_name_state:04}.png"))
                print(os.path.join(saved_dir, f"{image_name_state:04}.png"), "saved")
            except Exception as e:
                print(f"Error processing image: {e}")
    except Exception as e:
        print(f"Error fetching page: {e}")

    return image_name_state


def crawl_and_save_images_from_file(file_path, saved_dir, min_width, image_name_state):
    if not os.path.exists(os.path.join(saved_dir)):
        os.mkdir(os.path.join(saved_dir))

    with open(file_path, "r") as file:
        target_urls = [line.strip() for line in file if line.strip()]

    # Crawl all image URLs that meet the criteria
    cnt = 0
    print("num of urls =", len(target_urls))
    for url in target_urls:
        cnt += 1
        print(f"url {cnt}")
        url = url.strip()
        image_name_state = crawl_image_urls_from_a_page(
            url, min_width, saved_dir, image_name_state
        )
        print("Saving the images is done!")

    print("Crawl is done!")


# Specify the path to your text file containing URLs
url_file_path = "crawl_urls_part_9.txt"  # Replace with the actual path

saved_directory = "downloaded_images/4"  # Set your desired directory
minimum_width = 1000  # Set your minimum width threshold
image_state = 0  # Initialize image name state

crawl_and_save_images_from_file(
    url_file_path, saved_directory, minimum_width, image_state
)
