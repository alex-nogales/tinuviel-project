test = [1, 2, 5, 3, 7, 8, 6, 4]

'''
def minimuim_bribes(q):
    bribes = 0
    max_
    for index, _ in enumerate(q):
        deltas = [val < q[index] for val in q[index:]]
        delta = sum(deltas)
        
        if delta > 0:
            bribes = bribes + delta
        if delta >= 3:
            print('Too chaotic')
            return 
    print(bribes)



0 0
1 1
2 4
3 2
4 6
5 7
6 5
7 3

'''

def minimuim_bribes(q):
    bribes = 0
    q = [p-1 for p in q]
    for index, person in enumerate(q):
        if (person - (index)) > 2:
            print('Too chaotic')
            return
        # How many times a person has recieved a bribe
        for x in range(max(person-1, 0), index):
            if q[x] > person:
                bribes += 1

    print(bribes)

if __name__ == '__main__':
    minimuim_bribes(test)