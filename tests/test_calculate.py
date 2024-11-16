import pytest
from calculate import calc
import circle
import square

def test_calc_circle_area_valid():
    fig = 'circle'
    func = 'area'
    size = [5]

    result = calc(fig, func, size)
    expected = f'area of circle is {circle.area(5)}'
    assert result == expected

def test_calc_circle_perimeter_valid():
    fig = 'circle'
    func = 'perimeter'
    size = [5]

    result = calc(fig, func, size)
    expected = f'perimeter of circle is {circle.perimeter(5)}'
    assert result == expected

def test_calc_square_area_valid():
    fig = 'square'
    func = 'area'
    size = [4]

    result = calc(fig, func, size)
    expected = f'area of square is {square.area(4)}'
    assert result == expected

def test_calc_square_perimeter_valid():
    fig = 'square'
    func = 'perimeter'
    size = [4]

    result = calc(fig, func, size)
    expected = f'perimeter of square is {square.perimeter(4)}'
    assert result == expected

def test_calc_invalid_figure():
    fig = 'triangle'
    func = 'area'
    size = [3]

    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_calc_invalid_function():
    fig = 'circle'
    func = 'volume'
    size = [5]

    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_calc_invalid_size_for_circle():
    fig = 'circle'
    func = 'area'
    size = [-5]

    with pytest.raises(ValueError):
        calc(fig, func, size)

def test_calc_invalid_size_for_square():
    fig = 'square'
    func = 'perimeter'
    size = [-3]

    with pytest.raises(ValueError):
        calc(fig, func, size)
