# Testing

def print_hi(name):
    print(f'Hi, {name}')

# Spewcialized max function
# arr = [2, 5, 6, 1, 7, 4]

def my_bad_max(a_list):
    temp_max = 0
    counter = 0
    for index, num in enumerate(a_list):
        for other_num in a_list[0:index]:
            counter = counter + 1
            value = num - other_num
            if value > temp_max:
                temp_max = value

    print(f'I\'ve itrerated {counter} times...')
    return temp_max 

def my_good_max(a_list):
    temp_max = 0
    temp_max_value = 0
    counter = 0
    for value in reversed(a_list):
        counter = counter + 1
        if value > temp_max_value:
            temp_max_value = value
        if temp_max_value - value > temp_max:
            temp_max = temp_max_value - value

    print(f'I\'ve itrerated {counter} times...')
    return temp_max
    
if __name__ == '__main__':
    arr = [2, 5, 6, 1, 7, 4]
    print(my_good_max(arr))
