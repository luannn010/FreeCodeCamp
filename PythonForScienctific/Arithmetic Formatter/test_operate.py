from operate import Operator

def test_Calculation():
    problem1 = Operator(["11 + 9"])
    problem2 = Operator(["2 - 1"])
    assert problem1.calculate() == [20]
    assert problem2.calculate() == [1]

def test_WrongOperator():
    problem3 = Operator(["3 * 13"])
    problem4 = Operator(["10 / 5"])
    assert problem3.calculate() == "Error: Operator must be '+' or '-'."
    assert problem4.calculate() == "Error: Operator must be '+' or '-'."

def test_Over4digits():
    problem5 = Operator(["1001 + 2"])
    problem6 = Operator(["9 - 2009"])
    assert problem5.calculate() == "Error: Numbers cannot be more than four digits."
    assert problem6.calculate() == "Error: Numbers cannot be more than four digits."

def test_DigitsOnly():
    problem7 = Operator(["a + b"])
    problem8 = Operator(["9 + x"])
    assert problem7.calculate() == "Error: Numbers must only contain digits."
    assert problem8.calculate() == "Error: Numbers must only contain digits."


