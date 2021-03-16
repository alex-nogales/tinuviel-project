'''
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
without any duplicates. You are allowed to swap any two elements. Find the minimum number of
swaps required to sort the array in ascending order.
'''
arr = [4, 3, 1, 2]
# (0, 2) --> [1, 3, 4, 2]
# (1, 3) --> [1, 2, 4, 3]
# (2, 3) --> [1, 2, 3, 4]
# need 3 swaps

def minimum_swaps(arr):
    pivot, counter = 0, 0
    while pivot < len(arr):
        if arr[pivot] - 1 != pivot: # Swapt the numbers
            counter += 1
            temp_value = arr[arr[pivot] - 1]
            arr[arr[pivot] - 1] = arr[pivot]
            arr[pivot] = temp_value
        else:
            pivot += 1
    return counter
    

if __name__ == '__main__':
    print(minimum_swaps(arr))