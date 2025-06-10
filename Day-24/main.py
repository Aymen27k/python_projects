with open("my_file.txt", 'r') as file:
    data = file.read()
    print(data)
with open("my_file.txt", 'a') as file:
    text = f"\nSoon I will be a programmer"
    file.write(text)
