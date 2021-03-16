'''
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each the array element between two given indices,
inclusive. Once all operations have been performed, return the maximum value in the array.
'''
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

# Inneficient way to do this
def array_manipulation_bad(n, queries):
    # Create the vector with zero
    vector = [0 for _ in range(n)]
    max_val = -999
    for q in queries:
        for i in range(q[0], q[1] + 1):
            vector[i - 1] = vector[i - 1] + q[2]
            max_val = max(vector[i - 1], max_val)

    return max_val


# Efficent way to do this
def _inter(intervals, a, b, k):
    changes, current_index, new_intervales = a - b + 1, 0, []
    for interval in intervals:
        # no splitting
        if a > current_index + interval[0] or b < current_index:
            new_intervales.append(interval)
            continue

        # Split the interval --> [:a], [a, b], [b:]
        new_intervales.append([interval[1], ])


    return new_intervals


def array_manipulation(n, queries):
    # Create vector of zeros
    vector = [[n, 0]]
    
    # Process each query
    for q in queries:
        vector = _inter(vector, q[0] - 1, q[1] - 1, q[2])

    # Calculate max value
    max_value = -9999
    for interval in vector:
        max_value = max(max_value, interval[1])

    return max_value

 

if __name__ == '__main__':
    print(array_manipulation(n, queries))