
class Numerals:
    """
    Creates a instance of class numerals with
    an input
    """
    conversion_dict = {
                        "I": 1,
                        "V": 5,
                        "X": 10,
                        "C": 100,
                        "M": 1000
                        }

    def __init__(self, digits: str):
        """
        Initiales a property of digits and total
        :param digits: input from user passed to instance
        """
        self.digits = digits
        self.total = 0

    def convert_numerals(self) -> int:
        """
        Takes input from user and converts if to
        integer value
        :return: updates total property of instance
        """
        self.numeral_check()
        for char in self.digits:
            number = self.conversion_dict[char]
            self.total = self.total + number
        return self.total

    def numeral_check(self):
        """
        checks that a value given by user is accepted for
        application
        :return: nothing is OK, Error is NOK
        """
        accepted_values = list(self.conversion_dict.keys())
        digits = self.digits.upper()
        if not digits.isalpha():
            raise ValueError(
                'Ensure that input only contain characters and not digits'
            )
        for c in digits:
            if c not in accepted_values:
                raise ValueError(
                    'Ensure that input only contain Roman Numerals'
                )


def main(a: str) -> int:
    user_input = a
    conversion = Numerals(user_input)
    number_output = conversion.convert_numerals()
    return number_output


if __name__ == '__main__':
    main("XXX")
