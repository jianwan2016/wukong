# -*- coding: utf-8 -*-

import pytest
from wukong.skeleton import fib

__author__ = "Jian Wan"
__copyright__ = "Jian Wan"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
