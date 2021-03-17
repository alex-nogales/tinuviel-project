'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
'''
arr = [-4, 3, -9, 0, 4, 1]

def plus_minus(arr):
    positive_number, negative_number, zeroes = 0, 0, 0
    for num in arr:
        if num < 0:
            negative_number += 1
        elif num > 0:
            positive_number += 1
        else:
            zeroes += 1
    print('{:.6f}'.format(positive_number/len(arr)))
    print('{:.6f}'.format(negative_number/len(arr)))
    print('{:.6f}'.format(zeroes/len(arr)))


if __name__ == '__main__':
    print(plus_minus(arr))