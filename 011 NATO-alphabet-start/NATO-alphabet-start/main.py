student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row_data.letter: row_data.code for (row_index, row_data) in df.iterrows()}
while True:
    try:
        user_input = input("Enter a word: ").upper()
        word_list = [data_dic[letter] for letter in user_input]
        print(word_list)
        break
    except KeyError:
        print("Sorry, Only letter in the alphabet please.")
        continue
