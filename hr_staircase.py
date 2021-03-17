'''
Staircase detail
This is a staricase size n = 4:
   #
  ##
 ###
####

Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''
n = 4
def staircase(n):
    for i in range(1, n+1):
        print(('#' * i).rjust(n))


if __name__ == '__main__':
    print(staircase(n))