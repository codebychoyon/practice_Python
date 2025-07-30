
# n = int(input())

# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and n in range(2,5):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6,20):
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")


# leap year 

# year = int(input())

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
    
year = int(input())
print(is_leap_year(year))