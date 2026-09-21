from time import perf_counter

from quadratic_equation import parse_integer, solve


def test_ten_thousand_digit_solver_stays_within_budget() -> None:
    coefficient = "1" + "0" * 9_999

    started = perf_counter()
    result = solve("1", "0", "-" + coefficient)
    elapsed = perf_counter() - started

    assert result.status == "two_real"
    assert elapsed < 5.0


def test_oversized_input_is_rejected_before_solving() -> None:
    oversized = "1" + "0" * 10_000

    started = perf_counter()
    try:
        parse_integer(oversized)
    except ValueError as error:
        elapsed = perf_counter() - started
        assert "10,000" in str(error)
    else:
        raise AssertionError("an 10,001-digit coefficient must be rejected")

    assert elapsed < 0.1
