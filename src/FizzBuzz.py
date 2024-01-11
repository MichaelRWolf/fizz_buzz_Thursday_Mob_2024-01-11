# Forked from
# https://cyber-dojo.org/kata/edit/xJxHW1

def is_divisible_by(number, divisor):
    return number % divisor == 0


# def is_divisible_by_5(number):
#     return is_divisible_by(number, 5)
#
#
# def is_divisible_by_3(number):
#     return is_divisible_by(number, 3)
#
#
# def is_divisible_by_3_and_5(number):
#     return is_divisible_by_3(number) and is_divisible_by_5(number)


def get_word(divisor):
    def code_fn(code):
        def result(number):
            if is_divisible_by(number, divisor):
                return code
            else:
                return ""

        return result

    return code_fn


fizz = get_word(3)("Fizz")
buzz = get_word(5)("Buzz")
specs = [fizz, buzz]


def fizz_and_buzz(number):
    result = ""
    for spec in specs:
        result += spec(number)
    return result


def fizzbuzz(number):
    return fizz_and_buzz(number) or str(number)

class FizzBuzz():
