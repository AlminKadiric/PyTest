from calculator import Calculator
 
class TestCalculator:
     
    def test_isCorect(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        assert result == expected
 
 
    def test_isNegative(self):
        calc = Calculator()
        result = calc.sumFromNumbers(-4,1)
        expected = 0
        assert result < expected
 
 
    def test_isGreater(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        assert result >= expected
