#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt", 'r') as file:
    list_of_names = file.readlines()

with open("./input/Letters/starting_letter.txt", 'r') as letter_file:
    letter = letter_file.read()
    for name in list_of_names:
        stripped_name = name.strip()
        final_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(final_letter)

