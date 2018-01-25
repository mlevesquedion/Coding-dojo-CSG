import pytest
from solution import no_adjacent_integers

@pytest.mark.parametrize(
    ('lower', 'upper'),
    (
        (1, 6),
        (1, 9),
        (2, 10),
        (2, 11),
        (6, 105),
        (31, 151),
        (69, 120),
        (69, 87),
        (2, 196),
        (35, 101),
        (79, 130),
        (20, 130),
        (50, 157),
        (15, 71),
        (1, 10000001)
    )
)
def test_solution(lower, upper):
    ans = no_adjacent_integers(lower, upper)
    assert all(a not in (b - 1, b + 1) for a, b in zip(ans, ans[1:]) and sorted(ans) == range(lower, upper))
