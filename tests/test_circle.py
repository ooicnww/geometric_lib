import pytest
import math
from circle import area, perimeter


class TestCircle:
    def test_valid_circle_area(self):
        r = 3
        result = area(r)

        expected = math.pi * r * r
        assert result == pytest.approx(expected), \
            f"Expected area to be {expected} but got {result}"

    def test_zero_or_negative_radius_area(self):
        with pytest.raises(ValueError, match="The number is negative"):
            area(0)

        with pytest.raises(ValueError, match="The number is negative"):
            area(-2)

    def test_valid_circle_perimeter(self):
        r = 5
        result = perimeter(r)

        expected = 2 * math.pi * r
        assert result == pytest.approx(expected), \
            f"Expected perimeter to be {expected} but got {result}"

    def test_zero_or_negative_radius_perimeter(self):
        with pytest.raises(ValueError, match="The number is negative"):
            perimeter(0)

        with pytest.raises(ValueError, match="The number is negative"):
            perimeter(-1)
