# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

class FizzBuzz:

    def __init__(self):
        divisibility_rules = [
            (3, "Fizz"),
            (5, "Buzz")
        ]
        self.divisibility_checkers = [
            self.create_divisibility_checker(rule_number)(rule_string)
            for rule_number, rule_string
            in divisibility_rules
        ]

    def create_divisibility_checker(self, check_value):
        def divisibility_response(output_string):
            def check_and_return_output_string(number):
                if self.is_divisor_of(number, check_value):
                    return output_string
                else:
                    return ""

            return check_and_return_output_string

        return divisibility_response

    @staticmethod
    def is_divisor_of(number, divisor):
        return number % divisor == 0

    def fizz_and_buzz(self, number):
        result = ""
        for divisibility_checker in self.divisibility_checkers:
            result += divisibility_checker(number)
        return result

    def fizzbuzz(self, number):
        return self.fizz_and_buzz(number) or str(number)
