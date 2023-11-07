from PIL import Image, ImageOps
import threading


class CustomImage:
    def __init__(self, image_name, image_path):
        self.image_name = image_name
        self.image_path = image_path
        self.image = Image.open(image_path)

    def apply_grayscale_filter(self):
        self.image = ImageOps.grayscale(self.image)

    def save(self, path=None):
        if path is None:
            path = self.image_path
        self.image.save(path)


def process_images(image_objects):
    for img_obj in image_objects:
        img_obj.apply_grayscale_filter()
        img_obj.save()


if __name__ == "__main__":
    image_objects = [CustomImage(f"image_{i}", f"image_{i}.jpg") for i in range(10001)]

    chunk_size = len(image_objects) // 10
    threads = []

    for i in range(10):
        start_index = i * chunk_size
        if i == 9:
            end_index = None
        else:
            end_index = start_index + chunk_size

        thread = threading.Thread(
            target=process_images, args=(image_objects[start_index:end_index],)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Process completed.")
