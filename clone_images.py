from PIL import Image
import os


def generate_copies(input_image_path, output_directory, num_copies=10000):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with Image.open(input_image_path) as img:
        base_name = os.path.basename(input_image_path)
        name, ext = os.path.splitext(base_name)

        for i in range(num_copies):
            output_path = os.path.join(output_directory, f"image_{i}{ext}")
            img.save(output_path)
            print(f"Saved: {output_path}")


if __name__ == "__main__":
    INPUT_IMAGE = "image.jpg"
    OUTPUT_DIR = "."

    generate_copies(INPUT_IMAGE, OUTPUT_DIR)
