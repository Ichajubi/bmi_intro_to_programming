"""
Write the a python program that, 
given an input list of any level of complexity/nestedness, 
will return the inner most list plus 1. 
This is to be done with recursion. 
Note: the input will contain only integers or lists. 
"""

sample_list = [1,2,3,4,[5,6,7,[8,9]]]

def recursive_inner_plus(input_list):
    if isinstance(input_list[-1], list): #if the last element of the input_list is a list, calls the function again with the last element of the input_list
        return recursive_inner_plus(input_list[-1])
    else:
        return [num + 1 for num in input_list] #returns a new list adding 1 to each element of the inner most list
    
print(recursive_inner_plus(sample_list))

# #the code below also works, but is less readable even though it is more compact.
#    #if the last element of the input_list IS NOT a list, returns a new list adding 1 to each element of the inner most list. Otherwise, calls the function again with the last element of the input_list
# def recursive_inner_plus(input_list):
#    return [num + 1 for num in input_list] if not isinstance(input_list[-1], list) else recursive_inner_plus(input_list[-1]) 

# print(recursive_inner_plus(sample_list))

