# Left rotate an array by one place.

def rotated_array(data_list):
    temp = data_list[0]

    for i in range(1,len(data_list)):
        data_list[i-1] = data_list[i]

    data_list[len(data_list) - 1] = temp

list1 = [12, 14, 65, 18] #TestCase
rotated_array(list1)

print(f"Left Rotated Array: {list1}")
#Expected Output: [14, 65, 18, 12]

# Time Complexity: temp = data_list[0] takes O(1). The for loop iterates from i=1 up to, and does not include len(data_list). 
# it executes n - 1 times. The operation inside the loop (data_list[i-1] = data_list[i]) takes O(1) time per iteration. 
# Therefore, the loop contributes O(n) time. The overall time complexity is O(n).

# Space Complexity: O(1)
