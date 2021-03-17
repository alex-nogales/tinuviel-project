'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.
'''
n = 2
def flipping_bits(n):
    num = (2 ** 32) - 1
    return n ^ num


if __name__ == '__main__':
    print(flipping_bits(n))