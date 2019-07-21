import pytest

import run


class TestRomanNumerals:

    def test_main_app(self):
        result = run.Converter.main("XX")
        assert result == 20
