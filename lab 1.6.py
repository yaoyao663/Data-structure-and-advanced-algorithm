# The two passes with frequency disctionary

def find_first_occurrence(s):

    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for index, char in enumerate(s):
        if frequency[char] == 1:
            return index
    return -1   

# Test
s = "appleado"
result = find_first_occurrence(s)   
print(f"The index of the first non-repeating character in '{s}' is: {result}")

# The one pass with ordered dictionary

from collections import OrderedDict

def find_first_occurrence_orderer(s):
    frequency = OrderedDict()
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for char, count in frequency.items():
        if count == 1:
            return s.index(char)
    return -1

# Test
s = "appleado"
result = find_first_occurrence_orderer(s)   
print(f"The index of the first non-repeating character in '{s}' is: {result}")

