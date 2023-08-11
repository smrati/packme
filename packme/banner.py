import cv2
import numpy as np


class Banner:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self, text, output_path):
        # Create a NumPy array filled with white color (255, 255, 255)
        white_image = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255

        # Choose the font scale and color
        font_scale = 2
        font_color = (0, 0, 0)  # White color in BGR

        # Choose the font and putText parameters
        font = cv2.FONT_HERSHEY_SIMPLEX
        thickness = 5
        text_position = (10, 50)  # (x, y) position of the text on the image

        # Use the cv2.putText() function to write text on the image
        cv2.putText(white_image, text, text_position, font, font_scale, font_color, thickness)

        cv2.imwrite(output_path, white_image)

        return {"text": text, "output_image_path": output_path}


if __name__ == "__main__":
    b = Banner(600, 400)
    b.generate("Lorem ipsum", '/home/chick/Downloads/output.jpg')