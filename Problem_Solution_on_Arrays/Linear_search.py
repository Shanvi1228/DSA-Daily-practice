#To find a number by Linear Search.

def linear_search(list,num):  

    for i in range(0, len(list)):
        if(list[i] == num):
            return i
    return -1

#Test case
#list = [12,67,34,18,60]
#num = 18

result = linear_search(list, num)
print(result)

#Expected Output for the Testcase- 3
# Time Complexity- O(n) [worst case, avg case]
# Space Complexity- O(1)
