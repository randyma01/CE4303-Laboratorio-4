from PIL import Image, ImageOps


class CustomImage:
    def __init__(self, image_name, image_path):
        self.image_name = image_name
        self.image = Image.open(image_path)

    def apply_grayscale_filter(self):
        self.image = ImageOps.grayscale(self.image)
        self.image.show()

    def save(self, path):
        self.image.save(path)


if __name__ == "__main__":
    test_image = CustomImage("TestImage", "image.jpg")
    test_image.apply_grayscale_filter()
    test_image.save("grayscaled-image.jpg")
