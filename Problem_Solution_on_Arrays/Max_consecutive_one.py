# To find the Maximum Consecutive Ones(1).
#Optimal Approach 

def consecutive_num(data_list):
    maximum = 0
    count = 0
    for i in range (0, len(data_list)):
        if(data_list[i]==1):
            count += 1
            maximum = max(count,maximum)
        else:
            count = 0
    return maximum 

#TestCase
data_list = [1,0,1,1,1,0,4,1,1,3,1]

output = consecutive_num(data_list)
print(output)
#expected output- 3

#Time Complexity- O(N)
#Space Complexity- O(1)
