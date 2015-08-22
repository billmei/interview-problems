# Find median between two arrays if you combined them
# Both arrays are sorted

# [1,2,3,4,5] -> 3
# [4,5,6,7,8] -> 6
# [1,2,3,4,4,5,5,6,7,8] -> 4.5



# a + b

# x = [1,2,6,7,8,9,10] len = 7
# y = [1,2,3] len = 3

# x + y

# [1,1,2,2,3,6,7,8,9,10]

# Beat O(n/2) time and O(1) memory


def find_merged_median(arr1, arr2):
    # Where do I expect the median, given the two lengths?
    median_is_odd = (len(arr1) + len(arr2)) % 2 == 1
    
    expected_median_position = (len(arr1) + len(arr2)) // 2
    # arr1 = [5,6,7,100]
    # arr2 = [1,2]

    # Two pointers, and just walk until you get to your expected median position
    ptr1 = 0 # 0
    ptr2 = 0 # 1
    
    while ptr1 + ptr2 < expected_median_position:
        print (ptr1, ptr2)
        if ptr1 >= len(arr1):
            return arr2[expected_median_position - ptr1]
        elif ptr2 >= len(arr2):
            return arr1[expected_median_position - ptr2]
        
        
        if arr1[ptr1] > arr2[ptr2] and ptr2 < len(arr2):
            ptr2 += 1
        elif arr1[ptr1] < arr2[ptr2] and ptr1 < len(arr1):
            ptr1 += 1
        elif ptr2 < len(arr2):
            ptr1 += 1
        elif ptr1 < len(arr1):
            ptr2 += 1
    
    
    if arr1[ptr1] > arr2[ptr2] and median_is_odd:
        return arr2[ptr2]
    elif arr1[ptr1] < arr2[ptr2] and median_is_odd:
        return arr1[ptr1]
    
#     Skip the rest for now
#     elif ptr1 > ptr2 and not median_is_odd:
#         #arr1 = [2]
#         #arr2 = [1,3]
        

#     elif ptr1 < ptr2 and not median_is_odd:




assert find_merged_median([1,2,3,4], [4,5,6,7,8]) == 4
# assert find_merged_median([1,2,3,4,5], [4,5,6,7,8]) == 4.5
        