# Return the length of the longest word in the provided sentence.

# Your response should be a number.

def findLongestWordLength(str):
    length_list = []
    words = str.split(" ")
    for word in words:
        length_list.append(len(word))
    length_list.sort()
    return length_list[len(length_list) - 1]

print(findLongestWordLength("It's looking rough out there"))