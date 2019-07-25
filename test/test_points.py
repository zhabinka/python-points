# coding: utf-8

"""Tests for hexlet.pairs."""

from hexlet import points


def test_makeing_and_getting():
    """Test make_point + get_x + get_y."""
    p = points.make(1, -1)
    assert points.get_x(p) == 1, 'Should return a proper X.'
    assert points.get_y(p) == -1, 'Should return a proper Y.'


def test_to_string():
    """Test to_string conversion."""
    p = points.make(100, 200)  # noqa: WPS432
    assert points.to_string(p) == '(100, 200)', (
        'Should return a proper representation.'
    )
