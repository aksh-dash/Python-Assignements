dictionary = {"Alice": 35, "Bob": 30, "Charlie": 35}
name = input("Enter a name: ")
if name in dictionary:
    print(f"{name}'s marks: {dictionary[name]}")
else:
    print("Student not found.")