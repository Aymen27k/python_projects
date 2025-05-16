import math

test_h = int(input("Height of wall : "))
test_w = int(input("width of wall : "))

coverage = 5


def can_calc(height, width):
    number_cans = (height * width) / coverage
    rounded_up_cans = math.ceil(number_cans)
    print(f"You'll need {rounded_up_cans} cans of paint")


can_calc(test_h, test_w)
