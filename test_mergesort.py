import pytest
from hw2_debugging import merge_sort
invalid_inputs = [
    # Test case with None
    (None, TypeError, "Input must be a list"),
    # Test case with non-list input (integer)
    (42, TypeError, "Input must be a list"),
    # Test case with non-list input (string)
    ("invalid", TypeError, "Input must be a list"),
    # Test case with a dictionary
    ({"a": 1, "b": 2}, TypeError, "Input must be a list"),
    # Test case with mixed types (int and str)
    ([1, "two", 3], ValueError,
     "All elements in the list must be integers or floats"),
    # Test case with incompatible elements (int and list)
    ([1, [2, 3]], ValueError, "All elements in the list must be integers or floats"),
]

correctness_check_inputs = [
    ([3, 1, 2], [1, 2, 3]),  # Small unsorted list
    # Small unsorted list with more elements
    ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),
    ([10, 9, 8, 7, 6, 5], [5, 6, 7, 8, 9, 10]),  # Reversed list
    ([5, 5, 5, 5], [5, 5, 5, 5]),  # List with all elements equal
    ([6, 5, 10, 5, 6, 22], [5, 5, 6, 6, 10, 22]),  # Equal+not equal list
    # List with negative numbers
    ([-1, -5, -7, 9, 2, -29], [-29, -7, -5, -1, 2, 9])
]

corner_case_inputs = [
    # List with large positive and negative numbers
    ([1000000, 1, -1000000, 0, 999999], [-1000000, 0, 1, 999999, 1000000]),
    ([-1, -5, -3, -2], [-5, -3, -2, -1]),  # List with all negative numbers
    # List with negative floats
    ([1.5, 2.3, -0.7, -2.2, 0.0], [-2.2, -0.7, 0.0, 1.5, 2.3]),
    ([], []),  # Empty list
    ([1], [1]),  # Single element list
]


@pytest.mark.parametrize("input,expected_exception,expected_message",
                         invalid_inputs)
def test_merge_sort_invalid_inputs(
        input, expected_exception, expected_message):
    with pytest.raises(expected_exception) as exc_info:
        merge_sort(input)
    assert str(exc_info.value) == expected_message


@pytest.mark.parametrize("input,expected_output", correctness_check_inputs)
def test_merge_sort_correct_sorting(input, expected_output):
    print(merge_sort(input))
    assert merge_sort(input) == expected_output


@pytest.mark.parametrize("input,expected_output", correctness_check_inputs)
def test_merge_sort_correct_sorting(input, expected_output):
    assert merge_sort(input) == expected_output


@pytest.mark.parametrize("input,expected_output", corner_case_inputs)
def test_merge_sort_corner_cases(input, expected_output):
    assert merge_sort(input) == expected_output
