import unittest
from string_calculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):
    """
    Test class String Calculator if it calcuate correct result from string.
    """
    def setUp(self):
        self.calcuate = StringCalculator()

    def test_calculate_one_number(self):
        """
        Check correction of adding string with two numbers.
        """
        result = self.calcuate.calcuate('-3')
        expected_result = "-3"
        self.assertEqual(expected_result, result)

    def test_calculate_addition(self):
        """
        Check correction of adding string with two numbers.
        """
        result = self.calcuate.calcuate('1+4')
        expected_result = "5"
        self.assertEqual(expected_result, result)

    def test_calculate_addition_of_four_elements(self):
        """
        Check correction of adding string with four numbers.
        """
        result = self.calcuate.calcuate('15+4+10+3')
        expected_result = "32"
        self.assertEqual(expected_result, result)

    def test_calculate_subtraction(self):
        """
        Check correction of subtract string with two numbers.
        """
        result = self.calcuate.calcuate('10-8')
        expected_result = "2"
        self.assertEqual(expected_result, result)

    def test_calculate_subtraction_of_four_elements(self):
        """
        Check correction of subtract string with four numbers.
        """
        result = self.calcuate.calcuate('24-10-5-3')
        expected_result = "6"
        self.assertEqual(expected_result, result)

    def test_calculate_adding_and_subtraction(self):
        """
        Check correction of adding and subtract string.
        """
        result = self.calcuate.calcuate('8+20-5')
        expected_result = "23"
        self.assertEqual(expected_result, result)

    def test_calculate_subtraction_adding_subtraction(self):
        """
        Check correction of subtract adding subtraction string.
        """
        result = self.calcuate.calcuate('20-5+8-3')
        expected_result = "20"
        self.assertEqual(expected_result, result)

    def test_calculate_multiplication(self):
        """
        Check correction of multiply string with two numbers.
        """
        result = self.calcuate.calcuate('3x3')
        expected_result = "9"
        self.assertEqual(expected_result, result)

    def test_calculate_multiplication_and_adding(self):
        """
        Check correction order of operation.
        """
        result = self.calcuate.calcuate('1+2x3')
        expected_result = "7"
        self.assertEqual(expected_result, result)

    def test_calculate_order_multiplication_subtraction_adding(self):
        """
        Check correction order of operation for different operation.
        """
        result = self.calcuate.calcuate('11-2+4x3')
        expected_result = "21"
        self.assertEqual(expected_result, result)

    def test_calculate_all_operations(self):
        """
        Check correction order of operation for different operation.
        """
        result = self.calcuate.calcuate('11-2+4x3-5')
        expected_result = "16"
        self.assertEqual(expected_result, result)

    def test_calculate_adding_in_bracket(self):
        """
        Check correction order of operation in bracket.
        """
        result = self.calcuate.calcuate('(2+1)')
        expected_result = "3"
        self.assertEqual(expected_result, result)

    def test_calculate_bracket_at_the_beginning_and_multiplication(self):
        """
        Check correction order of operation with bracket at the beginning.
        """
        result = self.calcuate.calcuate('(2+1)x3')
        expected_result = "9"
        self.assertEqual(expected_result, result)

    def test_calculate_multiplication_and_bracket_at_the_end(self):
        """
        Check correction order of operation with bracket at the end.
        """
        result = self.calcuate.calcuate('2x(1+3)')
        expected_result = "8"
        self.assertEqual(expected_result, result)

    def test_calculate_two_operations_in_bracket(self):
        """
        Check correction two operations in bracket.
        """
        result = self.calcuate.calcuate('(2-5+7)x3-2')
        expected_result = "10"
        self.assertEqual(expected_result, result)

    def test_calculate_three_operations_in_bracket(self):
        """
        Check correction three operations in bracket.
        """
        result = self.calcuate.calcuate('(2x2+1+7)x3-2')
        expected_result = "34"
        self.assertEqual(expected_result, result)

    def test_calculate_correct_negative_num(self):
        """
        Check correction three operations in bracket.
        """
        result = self.calcuate.calcuate('2-5')
        expected_result = "-3"
        self.assertEqual(expected_result, result)

    def test_calculate_bracket_in_bracket(self):
        """
        Check correction three operations in bracket.
        """
        result = self.calcuate.calcuate('(2+(1+10)-1)')
        expected_result = "12"
        self.assertEqual(expected_result, result)

    def test_calculate_test(self):
        """
        Check correction three operations in bracket.
        """
        result = self.calcuate.calcuate('3+3+(4-3)')
        expected_result = "7"
        self.assertEqual(expected_result, result)
