# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

class FizzBuzz:

    def __init__(self):
        divisibility_rules = [
            (3, "Fizz"),
            (5, "Buzz")
        ]
        self.divisibility_checkers = [self.create_divisibility_checker(divisor)(outputString)
                                      for divisor, outputString
                                      in divisibility_rules]

    def create_divisibility_checker(self, check_value):
        def divisibilityResponse(outputString):
            def check_and_return_outputString(number):
                if self.is_divisible_by(number, check_value):
                    return outputString
                else:
                    return ""

            return check_and_return_outputString

        return divisibilityResponse

    def is_divisible_by(self, number, divisor):
        return number % divisor == 0

    def fizz_and_buzz(self, number):
        result = ""
        for divisibility_checker in self.divisibility_checkers:
            result += divisibility_checker(number)
        return result

    def fizzbuzz(self, number):
        return self.fizz_and_buzz(number) or str(number)
