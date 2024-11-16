import pytest
import math
from triangle import area, perimeter


class TestTriangle:
    def test_valid_triangle_area(self):
        a, b, c = 3, 4, 5

        result = area(a, b, c)

        assert math.isclose(result, 6.0), (
            f"Expected area to be 6.0 but got {result}"
        )

    def test_invalid_triangle_area(self):
        a, b, c = 1, 2, 3

        with pytest.raises(ValueError, match="The triangle cannot exist"):
            area(a, b, c)

    def test_negative_or_zero_sides_area(self):
        with pytest.raises(ValueError, match="The sides are negative"):
            area(0, 2, 3)

        with pytest.raises(ValueError, match="The sides are negative"):
            area(-1, 2, 3)

    def test_valid_triangle_perimeter(self):
        a, b, c = 3, 4, 5

        result = perimeter(a, b, c)

        assert result == 12, (
            f"Expected perimeter to be 12 but got {result}"
        )

    def test_negative_or_zero_sides_perimeter(self):
        with pytest.raises(ValueError, match="The sides are negative"):
            perimeter(0, 2, 3)

        with pytest.raises(ValueError, match="The sides are negative"):
            perimeter(-1, 2, 3)
