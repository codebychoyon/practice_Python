# Understanding & Working with Data Types in Python
import questionary


Name = "Farhan Shahriar Choyon" # string
age = 23
height = 5.9
is_student = True

print(f"Name is {Name}. Age is {age}. Height is {height}. Is he/she student - {is_student}")

print("Name is a ",type(Name))
print("age is a ", type(age))
print("height is a ", type(height))
print("Is he/she student ", type(is_student))

# input from user
Name = input("Name: ")
age = input("Age: ")
height = input("Height: ")
status = questionary.select(
    "Are you a student?",
    choices = ["student", "not student"]
).ask()

print(f"Name is {Name}. Age is {age}. Height is {height}. He/She is a {status}")




