from expression import Expression


class StringCalculator:
    """
    Class count mathematical operations from string

    """
    def calcuate(self, string_value):
        """
        Calculate math operations from string value

        :param string string_value: Input data

        :rtype: string
        """
        expression = Expression(string_value)
        string_value = expression.calculate_subexpressions(self.calcuate)
        if not self._is_number(string_value):
            expression = Expression(string_value)
            result = self._calculate_flat_operations(expression.get_chars())
            return self.calcuate(result)
        return string_value

    def _calculate_flat_operations(self, chars):
        """
        Calculate result from flat expression

        :param [str] chars: All chars from expression

        :rtype: str
        """
        math_operator = chars.index(self._find_math_operator(chars))
        first_number = int(chars[math_operator - 1])
        second_number = int(chars[math_operator + 1])
        result = self._calculate_result_for(first_number, chars[math_operator], second_number)
        del chars[math_operator - 1:math_operator + 2]
        chars.insert(math_operator - 1, str(result))
        return "".join(chars)

    def _find_math_operator(self, chars):
        """
        Find math operation in chars

        :param [str] chars: Numbers and math operators

        :rtype: str
        """
        math_operators = ['x', ['+', '-']]
        for operator in math_operators:
            for char in chars:
                math_operator = self._select_math_operator(char, operator)
                if math_operator:
                    return math_operator

    def _select_math_operator(self, char, operator):
        """
        Select math operator

        :param str char    : Char from expression
        :param str operator: Char of avaliable math operations

        :rtype: str
        """
        if char == operator:
            return operator
        for other in operator:
            if char == other:
                return other

    def _calculate_result_for(self, first_number, operator, second_number):
        """
        Chose operation base on operation char for two numbers

        :param str operator: Mathematical sign
        :param int first_number  : First number to calculate
        :param int second_number : Second number to calculate

        :rtype: int
        """
        if operator == "x":
            return self._multiplication(first_number, second_number)
        elif operator == "-":
            return self._subtraction(first_number, second_number)
        elif operator == "+":
            return self._addition(first_number, second_number)

    def _addition(self, first_number, second_number):
        """
        Addition two numbers

        :param int first_number : First number to calculate
        :param int second_number: Second number to calculate
        :rtype: int
        """
        return first_number + second_number

    def _subtraction(self, first_number, second_number):
        """
        Subtraction two numbers

        :param int first_number : First number to calculate
        :param int second_number: Second number to calculate

        :rtype: int
        """
        return first_number - second_number

    def _multiplication(self, first_number, second_number):
        """
        Multiplication two numbers

        :param int first_number : First number to calculate
        :param int second_number: Second number to calculate

        :rtype: int
        """
        return first_number * second_number

    def _remove_calculated_operation(self, chars, char_index):
        """
        Delete calculated numbers and math chars from lists

        :param [str] chars     : Numbers and math operations
        :param int   char_index: Index of counted operator

        :rtype: [str]
        """
        for i in range(0,3):
            chars.remove(chars[char_index-1])
        return chars

    def _is_number(self, string_value):
        """
        Check if char is convertable to int

        :param str string_value: Single char

        :rtype: bool
        """
        return string_value.strip('-').isdigit()
