#Left Rotate an array by D places.
#Optimal solution: By slicing Method.

def left_rotate_slicing(arr, d):
    
    n = len(arr)
    d = d % n # Handle rotations larger than the array length
    
    # The list is split at index d and the parts are concatenated
    return arr[d:] + arr[:d]

d = int(input("Enter the number of elements to left rotate: "))
arr = [12, 13, 15, 18, 20]

rotated_array = left_rotate_slicing(arr, d)

print(rotated_array)

# Time Complexity: O(n)
# Space Complexity: O(n)
