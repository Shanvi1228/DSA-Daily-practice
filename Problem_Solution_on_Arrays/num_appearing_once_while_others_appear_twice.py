#To find a number that appears once while all the other number appears twice.
#Optimal Approach 

def num_appearing_once(data_list):
     Xor = 0
     for i in range (0, len(data_list)):
        Xor = Xor ^ data_list[i]

     return Xor

data_list = [1, 1, 2, 3, 3, 4, 4]

output = num_appearing_once(data_list)
print(output)

#Time Complexity- O(N)
#Space Complexity- O(1)
