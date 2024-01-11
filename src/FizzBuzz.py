# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

class FizzBuzz:

    def __init__(self):
        self.specs = [self.get_word(3)("Fizz"), self.get_word(5)("Buzz")]

    def is_divisible_by(self, number, divisor):
        return number % divisor == 0

    def get_word(self, divisor):
        def code_fn(code):
            def result(number):
                if self.is_divisible_by(number, divisor):
                    return code
                else:
                    return ""

            return result

        return code_fn

    def fizz_and_buzz(self, number):
        result = ""
        for spec in self.specs:
            result += spec(number)
        return result

    def fizzbuzz(self, number):
        return self.fizz_and_buzz(number) or str(number)
