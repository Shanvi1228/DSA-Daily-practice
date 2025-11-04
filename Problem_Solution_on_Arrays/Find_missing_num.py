# To find the Missing number in an Array.
# Using the Brute force method approach.

def missing_num (data_list):
    N = len(data_list) + 1
    for i in range(1, N + 1):
        is_found = False
        for j in range(0, len(data_list)):
         if(data_list[j]==i):
            is_found = True
            break
         if not is_found: True
         return i
    return -1
  
#TestCase 1
data_list = [1, 2, 4, 5]
num = 3
missing_val = missing_num(data_list)
print(missing_val)
#expected output- 2

#Time complexity = O(N^2)
#Space complexity = O(1)
