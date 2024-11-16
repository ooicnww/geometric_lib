import pytest
from square import area, perimeter


class TestSquare:
    def test_valid_square_area(self):
        a = 5
        result = area(a)
        assert result == 25, f"Expected area to be 25 but got {result}"

    def test_zero_or_negative_side_area(self):
        with pytest.raises(ValueError, match="The side is negative"):
            area(0)

        with pytest.raises(ValueError, match="The side is negative"):
            area(-3)

    # Тест для функции perimeter
    def test_valid_square_perimeter(self):
        a = 7

        result = perimeter(a)

        assert result == 28, f"Expected perimeter to be 28 but got {result}"

    def test_zero_or_negative_side_perimeter(self):
        with pytest.raises(ValueError, match="The side is negative"):
            perimeter(0)

        with pytest.raises(ValueError, match="The side is negative"):
            perimeter(-5)
