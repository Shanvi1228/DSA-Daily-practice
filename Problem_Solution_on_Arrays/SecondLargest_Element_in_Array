# To find the Second Largest element in array.
# Approach- Optimal Approach 
# The algorithm finds the largest and second largest elements in a list by iterating through it only once. It maintains two variables, largest and slargest (second largest), updating them based on the current element.

class sdlargest:
    def find_sdlargest(self, data_list):
        if len(data_list) < 2:
            return "List must contain at least two elements"
            
        largest = data_list[0]
        slargest = None
    

        for i in range(1 ,len(data_list)):
            list_index = data_list[i]
            if(list_index>largest):
                slargest = largest
                largest = data_list[i]
            elif(list_index < largest and (slargest is None or list_index > slargest)):
                slargest = list_index
        return slargest
data_list = [10, 5, 20, 8, 15]         
solution = sdlargest()
solution.find_sdlargest(data_list)
result = solution.find_sdlargest(data_list) 


#Time Complexity- O(n)	
The algorithm iterates through the list once.

#Space Complexity- O(1)	
The algorithm uses only a few fixed-size variables (largest, slargest) regardless of the input size.


print(result)
