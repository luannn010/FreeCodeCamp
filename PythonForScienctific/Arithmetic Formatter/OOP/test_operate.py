import pytest
from OOP.operate import Operator

# Test case 1: Valid arithmetic operations
def test_operator_valid():
    operator = Operator(['2 + 3', '10 - 5'])
    expected_result = [5, 5]
    assert operator.calculate() == expected_result

# Test case 2: Numbers exceeding four digits
def test_operator_large_numbers():
    operator = Operator(['10000 + 10000'])
    expected_result = 'Error: Numbers cannot be more than four digits.'
    assert operator.calculate() == expected_result

# Test case 3: Non-digit characters in numbers
def test_operator_non_digits():
    operator = Operator(['3 + 8a'])
    expected_result = 'Error: Numbers must only contain digits.'
    assert operator.calculate() == expected_result

# Test case 4: Invalid operator
def test_operator_invalid_operator():
    operator = Operator(['5 * 2'])
    expected_result = 'Error: Operator must be \'+\' or \'-\'.'
    assert operator.calculate() == expected_result

# Test case 5: Too many problems
def test_operator_too_many_problems():
    operator = Operator(['2 + 3'] * 6)
    expected_result = 'Error: Too many problems.'
    assert operator.calculate() == expected_result

# Run the tests
if __name__ == '__main__':
    pytest.main()
