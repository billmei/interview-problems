def reverse_string(char_array):
    '''
    Reverse an array of characters in place
    '''
    left = 0
    right = len(char_array) - 1

    while left <= right:
        char_array[left], char_array[right] = \
        char_array[right], char_array[left]

        left += 1
        right -= 1

    return char_array

def test():
    assert reverse_string(list('hello world')) == list('dlrow olleh')
    assert reverse_string(list('')) == list('')
    assert reverse_string(list('a')) == list('a')
    assert reverse_string(list(u'abc')) == list(u'cba')
    print 'All tests pass'

test()
