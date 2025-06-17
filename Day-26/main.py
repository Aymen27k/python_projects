with open("file1.txt", 'r') as file:
    list1 = file.readlines()
with open("file2.txt", 'r') as file:
    list2 = file.readlines()
new_list1 = [int(n.strip()) for n in list1]
new_list2 = [int(n.strip()) for n in list2]

print(new_list1)
print(new_list2)
result = [n for n in new_list1 if n in new_list2]

print(result)
