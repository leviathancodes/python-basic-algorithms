# Reverse the provided string.

# You may need to turn the string into an array before you can reverse it.

# Your result must be a string.

def reverse_string(str):
    letters = list(str)
    letters.reverse()
    return "".join(letters)

print(reverse_string("hello"))