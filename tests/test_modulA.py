# https://docs.pytest.org/en/6.2.x/index.html

import pytest
from src.modulA import addition


def test_addition_result():
    assert addition(1, 2) == 3
    assert addition("a", "b") == "a---b"


def test_addition_formal():
    assert isinstance(addition(1, 2), int)
    assert isinstance(addition(1.5, 2), float)


@pytest.mark.parametrize("a, b, res",
                         [(1, 2, 3),
                          (1, 3, 4),
                          ("a", "b", "a---b")])
def test_addition_result_par(a, b, res):
    assert addition(a, b) == res