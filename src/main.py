# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

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


# Tests
def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"


def test_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


def test_numbers():
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
