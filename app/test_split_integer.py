from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    argument = 11223344

    result = sum(split_integer(argument, 4))
    expected = argument

    assert result == expected


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    argument = 64

    result = split_integer(argument, 8)
    expected = [8] * 8

    assert result == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    argument = 11

    result = split_integer(argument, 1)
    expected = [11]

    assert result == expected


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    argument = 17

    result = split_integer(argument, 4)
    expected = [4, 4, 4, 5]

    assert result == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 12) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
