import pytest
from solution import sum_integers_in_string

@pytest.mark.parametrize(
    ('string', 'expected'),
    (
    ("12.4", 16),
    ("h3ll0w0rld", 3),
    ("2 + 3 = ", 5),
    ("Our company made approximately 1 million in gross revenue last quarter.", 1),
    ("The Great Depression lasted from 1929 to 1939.", 3868),
    ("This string contains no integers.", 0),
    ("C4t5 are 4m4z1ng.", 18),
    ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635),
    ("qz@09*%c617fwxw?3$a403e70z?140", 1242),
    ("7%9u18?4*134194*03fb05lign5z9*", 134254),
    ("688)81w6bi0$7f#6y4897a34838374", 34844059),
    ("6913x%!mq97t&7mq9u#s3@3z0rq!7o", 7039),
    ("233t99nz18)31649l!znd83*98m6r$", 32186),
    ("175(i)5n!3$o9g)730*94)ix2w7n47", 1072),
    ("15(6m?65m$n34xhbnrdla0gwtxp9js", 129),
    ("0jytqi01$?a85t5l1bx1288%ps55y9", 1444),
    ("6620u3y@(1li25i1h&4368qt6at261", 11285),
    ("2@stk5k360jyodnw78v$1814k80e8b", 2347)
    )
)
def test_solution(string, expected):
    assert sum_integers_in_string(string) == expected
