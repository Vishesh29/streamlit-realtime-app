import cv2
import numpy as np
from PIL import Image, ImageFilter

def blur_image(image, radius=5):
    return image.filter(ImageFilter.GaussianBlur(radius))

def smooth_image(image):
    return image.filter(ImageFilter.SMOOTH)

def rotate_image(image, angle):
    return image.rotate(angle)

def crop_image(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))

def create_thumbnail(image, size=(128, 128)):
    image.thumbnail(size)
    return image

def convert_to_grayscale(image):
    return image.convert("L")

def resize_image(image, size):
    return image.resize(size)

def perspective_transform(image, points1, points2):
    img_np = np.array(image)
    matrix = cv2.getPerspectiveTransform(points1, points2)
    result = cv2.warpPerspective(img_np, matrix, (img_np.shape[1], img_np.shape[0]))
    return Image.fromarray(result)

