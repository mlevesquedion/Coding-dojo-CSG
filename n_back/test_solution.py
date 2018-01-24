import pytest
from solution import n_back

@pytest.mark.parametrize(
    ('sequence', 'n', 'expected'),
    (
        ([1, 1, 1, 1, 1], 1, 4),
        ([1, 1, 1, 1, 1], 2, 3),
        ([1, 2, 1, 2, 1], 1, 0),
        ([1, 2, 1, 2, 1], 2, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1], 9, 1),
        ([], 1, 0),
        ([1] * 1001, 1, 1000),
        ([1] * 1001, 1000, 1),
        ([9, 4, 3, 5, 6, 3, 4, 1, 8, 8, 1, 3, 8, 5, 2, 4, 2, 2, 9, 1, 6, 4, 5, 2, 7, 1, 3, 3, 4], 0, 29),
        ([7, 3, 9, 4, 6, 7, 8, 9, 3, 8, 7, 5, 2, 6, 8, 7, 2, 8, 6, 6, 7, 2, 3, 3, 9], 1, 2)
    )
)
def test_solution(n, sequence, expected):
    assert n_back(sequence, n) == expected
