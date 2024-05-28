from Calculator.Calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        a = 2000
        b = 1000
        cal = Calculator()

        result = cal.subtract(a,b)

        expected = 1000
        assert result == expected

    def test_multiply(self):
        a = 2
        b = 5
        cal = Calculator()

        result = cal.multiply(a,b)

        expected = 10
        assert result == expected

    def test_divide(self):
        a = 10
        b = 2
        cal = Calculator()

        result = cal.divide(a,b)

        expected = 5
        assert result == expected
    
    def test_0_divide(self):
        a = 10
        b = 0
        cal = Calculator()

        result = cal.divide(a,b)

        expected = ZeroDivisionError("Division by zero error")
        assert result == expected