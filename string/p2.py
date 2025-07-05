# Count character frequency in a string.

name = "Farhan Shahriar Choyon"

char_count = {}
# print (type(char_count))
for char in name:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

    print(f"Character: {char}, Count: {char_count[char]}")