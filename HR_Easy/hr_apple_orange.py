s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

def count_apples_orange(s, t, a, b, apples, oranges):
    ''' 
    :param s: starting point of sam's house
    :param t: end point of sam's house
    :param a: location of apple tree
    :param b: location of orange tree
    :param apples: array of distance at wich each apple falls from tree
    :param oranges: array of distance at wich each orange falls from tree
    ''' 
    apple_count, orange_count = 0, 0

    for apple in apples:
        apple_pos = a + apple
        if apple_pos >= s and apple_pos <= t:
            apple_count += 1

    for orange in oranges:
        orange_pos = b + orange
        if orange_pos >= s and orange_pos <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)



if __name__ == '__main__':
    print(count_apples_orange(s, t, a, b, apples, oranges))