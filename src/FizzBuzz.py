# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

class FizzBuzz:

    def __init__(self):
        divisibility_rules = [
            # (factor, string)
            (3, "Fizz"),
            (5, "Buzz")
        ]
        self.divisibility_checkers = [
            self.create_divisibility_checker(rule_factor)(rule_string)
            for rule_factor, rule_string
            in divisibility_rules
        ]

    def create_divisibility_checker(self, rule_factor):
        def divisibility_response(rule_string):
            def rule_string_for_number(n):
                # TMOWTDI - There's more than one way to do it...
                # 1 -- if/else
                # if self.is_factor_of(n, rule_factor):
                #     return rule_string
                # else:
                #     return ""
                #
                # 2 -- ternary
                # return rule_string if self.is_factor_of(n, rule_factor) else ""
                #
                # 3 -- and/or short-circuit logic
                return self.is_factor_of(n, rule_factor) and rule_string or ""

            return rule_string_for_number

        return divisibility_response

    @staticmethod
    def is_factor_of(number, divisor):
        return number % divisor == 0

    def fizz_and_buzz(self, number):
        # result = ""
        # for divisibility_checker in self.divisibility_checkers:
        #     result += divisibility_checker(number)
        result = ''.join(
            map(
                lambda checker: checker(number),
                self.divisibility_checkers)
        )
        return result

    def fizzbuzz(self, number):
        return self.fizz_and_buzz(number) or str(number)
