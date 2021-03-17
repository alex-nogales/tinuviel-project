'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

arr = [1, 3, 5, 7, 9]
def mini_max_sum(arr):
    summ = []
    for index in range(len(arr)):
        a = [x for i, x in enumerate(arr) if i!=index]
        summ.append(sum(a))

    print(min(summ), max(summ))

if __name__ == '__main__':
    print(mini_max_sum(arr))