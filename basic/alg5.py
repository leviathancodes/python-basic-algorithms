# Basic Algorithm Scripting: Return Largest Numbers in Lists
# Return a list consisting of the largest number from each provided sub-list. For simplicity, the provided list will contain exactly 4 sub-lists.

# Remember, you can iterate through an list with a simple for loop, and access each member with list syntax list[i].

def largest_of_four(list):
    largest_numbers = []
    for lists in list:
        lists.sort()
        largest_numbers.append(lists[len(lists) - 1])
    
    return largest_numbers

print(largest_of_four([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]))