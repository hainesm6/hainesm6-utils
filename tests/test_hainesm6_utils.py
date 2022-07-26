#!/usr/bin/env python
"""Tests for `hainesm6_utils` package."""

import pytest

import hainesm6_utils as hu


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_experimental_power():
    lower_power = hu.experimental_power(n_treatments=5, practical_diff=0.2 * 16.8389, variance=1.1378, replicates=2)
    upper_power = hu.experimental_power(n_treatments=5, practical_diff=0.2 * 16.8389, variance=1.1378, replicates=6)
    assert round(lower_power, 2) == 0.35
    assert round(upper_power, 2) == 0.99
