'''
Given a 6 x 6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g

There are 116 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, 
then print the maximum hourglass sum. The array will always be 6 x 6.

Example

arr ==

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

The 16 hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

0 4 3
  1
8 6 6

'''
hourglass = [[1,1,1], [0,1,0], [1,1,1]]
test_arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# Simple function that makes point to point multiplication and sum
def _conv(_arr, _filter, _i, _j):
    total_sum = 0
    for i in range(3):
        for j in range(3):
            total_sum = total_sum + _arr[i + _i][j + _j] * _filter[i][j]
    return total_sum


def max_hourglass(arr):
    max_conv = -999
    for i in range(4):
        for j in range(4):
            max_conv = max(max_conv, _conv(arr, hourglass, i, j))
    return max_conv

if __name__ == '__main__':
    print(max_hourglass(test_arr))