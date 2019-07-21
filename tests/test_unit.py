import pytest

import run
import app.Converter as Converter

test_data = [("XCX", 120),
             ("VMX", 1015),
             ("XMX", 1020),
             ("X", 10),
             ("XXII", 22),
             ("CMXX", 1120),
             ("CMMXMMX", 4120)
             ]


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
