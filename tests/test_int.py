import pytest
import sys
import run

test_data = [("XCX", 120),
             ("X", 10),
             ("CMXX", 1120),
             ("CMMXMMX", 4120)
             ]


class TestRomanNumerals:

    @pytest.mark.parametrize('roman, result', test_data)
    def test_main_app(self, roman, result):
        """
        Parameterised test of the main method of application
        """
        result = run.Converter.main(roman)
        assert result == result

    @pytest.mark.parametrize('roman, result', test_data)
    def test_main_input(self, roman, result, monkeypatch):
        """
        Parameterised test of sys inputs from command line
        """
        with monkeypatch.context() as m:
            m.setattr(sys, 'argv', ['run', roman])
            assert run.main() == result


