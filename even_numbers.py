sum_of_even_numbers = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum_of_even_numbers += number
    number += 1

print(f"The sum of even Numbers is {sum_of_even_numbers}")


