import pytest
from OOP.demo import arithmetic_arranger

# Test case 1: Valid arithmetic problems
def test_arithmetic_arranger_valid():
    arranger = arithmetic_arranger(['2 + 3', '10 - 5'])
    expected_output = '   2      10\n+  3    -  5\n----    ----'
    assert str(arranger) == expected_output

# Test case 2: Numbers exceeding four digits
def test_arithmetic_arranger_large_numbers():
    arranger = arithmetic_arranger(['10000 + 10000'])
    expected_output = 'Error: Numbers cannot be more than four digits.'
    assert str(arranger) == expected_output

# Test case 3: Non-digit characters in numbers
def test_arithmetic_arranger_non_digits():
    arranger = arithmetic_arranger(['3 + 8a'])
    expected_output = 'Error: Numbers must only contain digits.'
    assert str(arranger) == expected_output

# Test case 4: Invalid operator
def test_arithmetic_arranger_invalid_operator():
    arranger = arithmetic_arranger(['5 * 2'])
    expected_output = 'Error: Operator must be \'+\' or \'-\'.'
    assert str(arranger) == expected_output

# Test case 5: Too many problems
def test_arithmetic_arranger_too_many_problems():
    arranger = arithmetic_arranger(['2 + 3'] * 6)
    expected_output = 'Error: Too many problems.'
    assert str(arranger) == expected_output

# Test case 6: Arithmetic problems with solutions
def test_arithmetic_arranger_with_solutions():
    arranger = arithmetic_arranger(['2 + 3', '10 - 5'], bool=True)
    expected_output = '   2      10\n+  3    -  5\n----    ----\n   5       5'
    assert str(arranger) == expected_output

# Run the tests
if __name__ == '__main__':
    pytest.main()
