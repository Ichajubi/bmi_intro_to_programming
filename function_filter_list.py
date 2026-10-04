"""
Write a Python program that defines a standard function to filter a list of numbers. 
The function should accept two arguments:
1. A list of numbers
2. A user-defined threshold value
The function should return a new list containing only the numbers that are less than or equal to the specified threshold. 
Values greater than the threshold should be excluded.
"""

unordered_list = [1,5,3,8,2,7,4,6,9,10,14,12,11,15,13,17,16,18,20,19]
sample_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
threshold = int(input("Enter a threshold value: ")) #asks for user input for the threshold value and converts it to an integer
#threshold = 12

def filter_list(input_list, threshold):
    filtered_list = []
    for num in input_list:
        if num <= threshold:
            filtered_list.append(num) #appends value to the filtered list if it is less than or equal to the threshold

    return sorted(filtered_list) #returns the filtered list with values sorted in ascending order

print(filter_list(sample_list, threshold))
print(filter_list(unordered_list, threshold)) #I wanted to check that the function appropriately sorted an unordered list as well as a pre-sorted list.