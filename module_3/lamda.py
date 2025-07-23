# lamda function

# lamda agrguments: expression

# Lambda function
y = lambda a, b: a + 10 + b # only one expression 
print(y(5, 6))


# normal function
def y(a,b):
    return a + 10, b + 20
result = y(a = 6, b = 7) # keyword arguments
print(result)
print(type(result))