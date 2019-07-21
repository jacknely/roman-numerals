"""
Application that takes a Roman Numeral from command
line input and returns its numerical equivalent.
Input form: python: [run.py] [Roman Numeral]
example: run.py XXX
result: 30
"""

import app.Converter as Converter
import sys


if __name__ == '__main__':
    try:
        a = sys.argv[1]
        result = Converter.main(a)
        print(result)
    except Exception as error:
        print(error)
