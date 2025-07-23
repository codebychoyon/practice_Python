# Function is a simple task list that can be reused 

def make_tea():
    print("Making tea...")
    print("Steeping tea leaves...")
    print("Adding sugar and milk...")
    print("Your tea is ready!")

make_tea()


x = 5

def my_function():
    global x
    print("X IS LOCAL ", x)

my_function()
print("X is global ", x)

