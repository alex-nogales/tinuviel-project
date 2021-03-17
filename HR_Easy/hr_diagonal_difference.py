'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
1 2 3 
4 5 6
8 7 9

11 2 4
4 5 6
10 8 -12
'''

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonal_difference(arr):
    a_diagonal, b_diagonal = 0, 0
    for i, _ in enumerate(arr):
        a_diagonal += arr[i][i]
        b_diagonal += arr[i][(len(arr) - 1) - i]
    
    return abs(a_diagonal - b_diagonal)



if __name__ == '__main__':
    print(diagonal_difference(arr))