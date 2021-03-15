# Rotate array to the left\
arr = [1, 2, 3, 4, 5]
def rot_left(a, d):
    '''
    :param a: array
    :param d: rotation count
    '''
    return a[d:] + a[:d]

if __name__ == '__main__':
    print(rot_left(arr, 1090))
    
