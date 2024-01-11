# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

class FizzBuzz:

    def __init__(self):
        self.specs = [self.create_divisibility_checker(3)("Fizz"), self.create_divisibility_checker(5)("Buzz")]

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
        for spec in self.specs:
            result += spec(number)
        return result

    def fizzbuzz(self, number):
        return self.fizz_and_buzz(number) or str(number)
