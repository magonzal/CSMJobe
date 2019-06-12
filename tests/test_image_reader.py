import pytest
from src.digitizer.image_reader import ImageReader
import cv2
import numpy as np


@pytest.fixture()
def image():
    image_to_test = cv2.imread('test3.jpg')
    return image_to_test


def test_get_image(image):
    test_one = ImageReader(image)
    case_one = cv2.imread('test3.jpg')

    assert type(test_one.get_image()) == np.ndarray
    assert test_one.get_image().shape == (650, 104, case_one.shape[2])


def test_set_image(image):
    test_one = ImageReader(image)


def test_prune():
    pass

def test_filter():
    pass

def test_gaussian_blur():
    pass

def test_average_blur():
    pass


