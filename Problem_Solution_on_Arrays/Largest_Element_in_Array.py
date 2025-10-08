#TO FIND THE LARGEST ELEMENT IN AN ARRAY 
#Approach - Optimal Iterative Solution.
# We initialize the 'largest' variable with the first element and iterate through 
# the rest of the array, updating 'largest' whenever a greater element is found.

def find_largest(my_list):
    if not my_list:
        return None 

    largest = my_list[0]
    for i in range (len(my_list)):
  
        if(my_list[i] > largest):
            largest = my_list[i]
    return largest

# Example Test Cases:
# print(find_largest([12, 13, 3, 54, 14])) # Output: 54
# print(find_largest([])) # Output: None

#Time Complexity- O(N)
# - We visit every element in the array exactly once.
#Space Complexity- O(1)
#   - We only use a constant amount of extra space (one variable 'largest') 
#     regardless of the array size.
