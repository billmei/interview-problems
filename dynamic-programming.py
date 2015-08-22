#!/usr/bin/env python

my_string = '''34
43 19
92 73 01
12 07 38 06
12 22 04 56 88'''


def find_max_path(input_str):
    input_str = input_str.strip().splitlines()

    prev_row = [0]
    for row in input_str:
        row = [int(num) for num in row.strip().split(' ')]

        # Sum the current number with its parents (pick the max parent)
        # Carry the sum forward to the next row
        # Once we get to the last row, return the max element in the row
        for i in xrange(len(row)):
            if i == 0:
                # Left edge
                row[i] += prev_row[i]
            elif i == len(row) - 1:
                # Right edge
                row[i] += prev_row[i-1]
            else:
                # Middle
                row[i] += max(prev_row[i], prev_row[i-1])

        prev_row = row

    return max(prev_row)


print find_max_path(my_string)
