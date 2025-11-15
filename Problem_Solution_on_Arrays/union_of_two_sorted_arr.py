#By using a Loop.
#Brute force Method.

def union_arr(data_list1, data_list2):
    data_list3 = [] 
    
    for element in data_list1:
        if element not in data_list3:
            data_list3.append(element)       

    for element in data_list2:
        if element not in data_list3:
            data_list3.append(element)        
    return data_list3

data_list1 = [1, 1, 2, 3, 4, 5]
data_list2 = [1, 4, 4, 5, 6]
sol = union_arr(data_list1, data_list2)
print(sol)
# Output: [1, 2, 3, 4, 5, 6]

# -------------------------------------------------

#BY using the sets.
#Optimal Method.

def union_arr(data_list1, data_list2):

    set1 = set(data_list1)
    set2 = set(data_list2)
    
    union_set = set1 | set2
    
    data_list3 = list(union_set)
    return data_list3

data_list1 = [1, 1, 2, 3, 4, 5]
data_list2 = [1, 4, 4, 5, 6]

sol = union_arr(data_list1, data_list2)
print(sol)



