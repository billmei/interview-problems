
def intersection(array_1, array_2):
    intersection = []
    for item_1 in array_1:
        for item_2 in array_2:
            if item_1 == item_2:
                intersection.append(item_1)

    return intersection



arr_1 = [1, 4, 2, 6, 10]
arr_2 = [7, 4, 9, 10, 20]
result = [4, 10]

assert intersection(arr_1, arr_2) == result
print "all tests pass"