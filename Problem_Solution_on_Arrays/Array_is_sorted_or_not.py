# Check if the Array is sorted or not 

def sorted_array(data_list):
    for i in range(1, len(data_list)):
        if(data_list[i]<=data_list[i-1]):
            return "Not Sorted"
       
    return True


# Test Cases        
list1 = [12,13,15,16,18]
list2 =[12,43,23,14,17]

result1 = sorted_array(list1)
result2 = sorted_array(list2)
print(result1)
print(result2)

# Time Complexity: O(n)
# Space Complexity: O(1)
