num = 15  # int
num_f = 3.42  # float
num_c = 1j  # complex
print(num)
print(num_f)
print(num_c)
print(2 * (5 * 3))
x = float(num)
y = complex(num_f)
z = complex(num)
print(type(x))
print(type(y))
print(type(z))

two_digit_numbers = input("Type a two digit number: ")

first_digit = two_digit_numbers[0]
second_digit = two_digit_numbers[1]

print(int(first_digit) + int(second_digit))
