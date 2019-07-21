import pytest

import app.Converter as Converter

test_data = [("XCX", 120),
             ("VMX", 1015),
             ("XMX", 1020),
             ("X", 10),
             ("XXII", 22),
             ("CMXX", 1120),
             ("CMMXMMX", 4120)
             ]

test_error_str = ["Xrr", "yu", "jk"]

test_error_dig = ["Xrr4", "4", "5789"]


class TestRomanNumerals:

    def setup_method(self):
        """
        Setup a instance of class Numeral for testing
        """
        self.test_conversion = Converter.Numerals("X")

    @pytest.mark.parametrize('roman, result', test_data)
    def test_convert_numerals(self, roman, result):
        self.test_conversion.digits = roman
        test_number_output = self.test_conversion.convert_numerals()
        assert test_number_output == result

    @pytest.mark.parametrize('char', test_error_str)
    def test_number_check(self, char):
        with pytest.raises(ValueError) as excinfo:
            self.test_conversion.digits = char
            self.test_conversion.numeral_check()
        assert 'Ensure that input only contain Roman Numerals' in str(excinfo.value)

    @pytest.mark.parametrize('digit', test_error_dig)
    def test_number_check(self, digit):
        with pytest.raises(ValueError) as excinfo:
            self.test_conversion.digits = digit
            self.test_conversion.numeral_check()
        assert 'Ensure that input only contain ' \
               'characters and not digits' in str(excinfo.value)
