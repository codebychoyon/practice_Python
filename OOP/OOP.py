# Object Oriented Programming (OOP) in Python

# class Car:
    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color

#     def greet(self, name, color):
#         self.name = name
#         self.color = color
#         print(f"Hello, This is a car! Its name is {self.name}, color is {self.color}")

# car1 = Car()

# car1.greet("farari", "red")

# car2 = Car()

# print(car1)
# print(type(car2))

# car1.__init__("Farari", "Red")
# car1.greet()


# class Blog:
#     def show_blog(self):
#         print(self.title)
#         print("<->"*4)
#         print(self.description)

# b1 = Blog() # instance or object

# b1.title = "First Blog" # here <title> is a property or attribute of b1 object.
# b1.description = "This is my first blog. I am excited to share it with you all." # here <description> is a property or attribute of b1 object.

# # print(b1.title, b1.description)

# b1.show_blog()


# class variablr and instance variable

# class School:
#     school_name = "Softvence" # class Variable

#     def students(self, student_name):
#         self.student_name = student_name # object variable or instance variable
#         print(f"Hello, {self.student_name} welcome to {self.school_name}")

# s1 = School()

# s1.students("choyon")

# print(s1.school_name)


# constructor

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def login(self):
#         print(f"{self.username} logged in")
    
#     def show_email(self):
#         print(f"{self.username}'s email is {self.email}")

# u1 = User("Choyon", "choyon@gmail.com")
# u1.login()
# u1.show_email()


# property decorator

class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

u1 = User("Farhan", "Shahriar")

print(u1.full_name) 