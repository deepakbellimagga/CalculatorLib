import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_additionone(self):
        assert 5 == calculator.add(2, 3)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
