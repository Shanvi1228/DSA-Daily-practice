#To find the missing number by Optimal Approach.

def missing_num(data_list):
    N = len(data_list) + 1
    
    total_sum = (N*(N+1))//2
        
    data_sum =  sum(data_list)

    missing_val = total_sum - data_sum
    return missing_val
  
#TestCase
data_list = [1, 2, 4, 5]
result = missing_num(data_list)

print(result)
#Expected Output- 3

#Time Complexity - O(N)
#Space Complexity - O(1)
