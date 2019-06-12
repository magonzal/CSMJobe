import pytest
from src.digitizer.point import Point


def test_get_point():
    point = Point(2,2)

    assert point.x == 2
    assert point.y == 2


def test_set_point():
    point = Point(4, 2)
    point.x = 5
    point.y = 10

    assert point.x == 5
    assert point.y == 10
