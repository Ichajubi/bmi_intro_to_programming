#Problem 1.a
def wrong_add_function(arg1,arg2):
   arg1_index=0
   #print(f'starting index is: {arg1_index}')
   #print(f'The correct starting index should be: 0')
   
   while arg1_index < len(arg1):
      #print(f'Current index is: {arg1_index}')
      #print(f'The correct index should be: arg1_index')
      arg_2_sum = 0
      #print(arg_2_sum)
      
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print(f'\n1.a = We are making an error in this loop arg_2_sum is: {arg_2_sum}')
         print(f'1.a = The correct arg_2_sum should be: {arg1[arg1_index] + arg2[arg1_index]}')
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]
wrong_add_function(arg1, arg2)



#Problem 1.b
def correct_add_function(arg1, arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]
print(f'\n1.b = {correct_add_function(arg1, arg2)}')




#Problem 2.a        
def wrong_add_function(arg1,arg2):
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1',1]


#Problem 2.b
def exception_add_function(arg1, arg2):
    try:
        expected_type = int #define the expected type for the numeric section
        # Check that each list contains only integers
        for argument_num, argument in enumerate([arg1, arg2], start=1):
            for element_index, element in enumerate(argument):
                if type(element) != expected_type:
                    raise TypeError(
                        f"Your input argument {argument_num} at element {element_index} is not of the expected type. "
                        f"Please change this and rerun."
                    )
        return exception_add_function(arg1, arg2)
    except TypeError as error:
        print(f'2b = {error}')

exception_add_function(arg_str_1,arg_str_2)


#Problem 2.c
def correction_add_function(arg1, arg2):
    try:
        # Check if all elements in arg1 and arg2 are strings
        if all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
            return wrong_add_function(arg1, arg2)
        else:
            raise TypeError("Input lists must contain only strings.")
    except TypeError as error:
        print(f'2c = {error}')

correction_add_function(arg_str_1, arg_str_2)