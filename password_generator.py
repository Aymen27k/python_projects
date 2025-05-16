import random

# Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to 'Aymen Kalaï Ezar' Password Generator!")
nr_letters = int(input(f"How many letters would you like in your password ? \n"))
nr_symbols = int(input(f"How many symbols would you like in your password ? \n"))
nr_numbers = int(input(f"How many numbers would you like in your password ? \n"))

password_list = []

for letter in range(nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

for number in range(nr_numbers):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

random.shuffle(password_list)
final_password = "".join(password_list)


def password_strength():
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    # Flagging charaters type of the password
    for char in final_password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True
    length = len(final_password)
    variety_count = has_lower + has_upper + has_digit + has_symbol
    if length < 8:
        print("Your password is too short")
        if variety_count <= 1:
            print("It also lacks sufficient variety. Consider making it longer and using different types of "
                  "characters for better security.")
        elif variety_count == 4:
            print("While short, it has some variety. However, a longer password is highly recommended for better "
                  "security.")
        else:
            print("Your password variety could be better, please reconsider another one")
    elif length < 12:
        if variety_count < 2:
            print(
                "Your password has moderate length but lacks sufficient variety. Consider adding more character types.")
        elif variety_count < 3:
            print("Your password has moderate strength.")
        else:
            print("Your password has good moderate strength due to its variety.")
    elif length < 16:
        if variety_count < 3:
            print("Your password has good length but could be stronger with more character types.")
        else:
            print("Your password is strong.")
    else:
        if variety_count < 4:
            print("Your password has excellent length but could be even more secure with all four character types.")
        else:
            print("Your password is very strong and highly secure!")



print(f"Here is your Password : {final_password}")
password_strength()
