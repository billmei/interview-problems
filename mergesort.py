from __future__ import print_function
import random

def main():
    print(test())

def mergesort(array):
    temp_array = [None] * len(array)

    
    
    return array


def test():
    my_array = [i for i in range(20)]
    random.shuffle(my_array)
    assert mergesort(my_array) == my_array
    assert mergesort([]) == []
    assert mergesort([0]) == [0]
    return "All tests passed"

if __name__ == '__main__':
    main()