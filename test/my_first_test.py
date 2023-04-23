import pytest
from programs.my_prog import RegularPolygon
def test_get_perimeter_result():
    polygon = RegularPolygon(3,5)
    assert polygon.get_perimeter(polygon) == 15
    assert RegularPolygon.get_perimeter(polygon) == 15

