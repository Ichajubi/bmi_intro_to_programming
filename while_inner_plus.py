"""
Write a python program that, 
given an input list of any level of complexity/nestedness, 
will return the inner most list plus 1.
This is to be done with a while loop. Note: the input will contain only integers or lists.

As an example:

your_py_program.py input_list
will produce:
[9,10]
That is [8, 9] (the inner most list) plus 1 -> [9, 10]
"""

sample_list = [1,2,3,4,[5,6,7,[8,9]]]

def while_inner_plus(input_list): #defines the function while_inner_plus that takes a list as input
    while isinstance(input_list[-1], list): #while the last element (input_list[-1]) is a list, continues to loop
        input_list = input_list[-1] #assigns the last element of the input_list to input_list and loops back, effectively "drilling down" into the nested lists
    return [num + 1 for num in input_list] #returns a new list adding 1 to each element of the inner most list

print(while_inner_plus(sample_list))