#Promt the user for input
user_string = input("Enter a string to write into the file: ")
#Create and open the file in write mode ('w')
with open("user_input.txt", "w") as file:
    #Write the user's input to the file
    file.write(user_string)
add_more = input("Would you like to add more to the file (yes/no)").lower()
#In case the user type "YES" We append more string into the .txt
data = "" #Creating the data var to make it accesible in all statements
if add_more == "yes":
    additional_string = input("Enter the text to add: ")
    with open("user_input.txt", "a") as file:
        file.write("\n"+additional_string)
    # Print a confirmation message
    with open ("user_input.txt",'r') as file:
        data = file.read()
        print(data)
elif add_more == "no":
    print("No extra text needed")
    data = user_string
    print(data)
else:
    print("Invalid input. Please enter 'yes' or 'no'.")

