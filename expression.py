import re


class Expression:
    """
    Class find expressions and prepare it for counting.

    :param str string_value: Mathematical operation in string type
    :param int start       : Start index of expression
    :param int end         : End index of expression
    """
    def __init__(self, string_value, start=0, end=0):
        self._string_value = string_value
        self._start = start
        self._end = end

    def calculate_subexpressions(self, calculate):
        """
        Calculate subexpressions and replace it by result

        :param function calculate: Method for calculate string

        :rtype: str
        """
        subexpressions = self.find_expressions()
        if not self._string_value.count("(") > 0:
            return self._string_value
        for subexpression in subexpressions:
            subexpression_result = calculate(subexpression._string_value)
            string_value = self.replace_subexpression(subexpression, subexpression_result)
        return string_value


    def find_expressions(self):
        """
        Finding subexpressions in string and create list of them

        :rtype: [Expression]
        """
        chars = self.get_chars()
        expressions = []
        while "(" in chars:
            start, end = self._find_expressions_positions(chars)
            subexpression = chars[start + 1: end]
            expressions.append(Expression("".join(subexpression), start, end))
            del chars[start:end + 1]
        return expressions

    def _find_expressions_positions(self, chars):
        """
        Find opening and closing bracket indexes in string

        :param [str] chars: Numbers and math chars

        :rtype: [int]
        """
        open_brackets = [i for i in range(len(chars)) if chars[i] == "("]
        close_brackets = [i for i in range(len(chars)) if chars[i] == ")"]
        if len(open_brackets) >= 2:
            for open_bracket in open_brackets[1:len(open_brackets)]:
                if close_brackets[0] < open_bracket:
                    return open_brackets[0], close_brackets[0]
        return open_brackets[0], close_brackets[-1]

    def replace_subexpression(self, subexpression, result):
        """
        Replace result to position of subexpression

        :param Expression subexpression: Expression which we replace
        :param str        result       : Calculated result of subexpression

        :rtype: str
        """
        chars = self.get_chars()
        del chars[subexpression._start:subexpression._end + 1]
        chars.insert(subexpression._start, str(result))
        self._string_value = "".join(chars)
        return self._string_value

    def get_chars(self):
        """
        Split string for numbers and chars and save it to list

        :rtype: [str]
        """
        chars = re.findall('[\d,(,),x,+,-]', self._string_value)
        numbers_and_chars =[]
        if chars[0] == "-":
            numbers_and_chars.append(str(chars[0])+str(chars[1]))
            del chars[0:2]
        self._join_digits_to_numbers(chars, numbers_and_chars)
        return numbers_and_chars

    def _join_digits_to_numbers(self, chars, numbers_and_chars):
        """
        Join digits to numbers

        :param [str] chars            : All chars from string
        :param [str] numbers_and_chars: Only joined numbers with math operators

        :rtype: None
        """
        number = ""
        for char in chars:
            if self._is_number(char):
                number += char
            else:
                if number:
                    numbers_and_chars.append(str(number))
                numbers_and_chars.append(char)
                number = ""
        if number:
            numbers_and_chars.append(str(number))

    def _is_number(self, string_value):
        """
        Check if it's possible convert char to integer

        :param str string_value: Single char

        :rtype: bool
        """
        return string_value.strip('-').isdigit()
