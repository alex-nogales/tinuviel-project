'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example

steps = 8 path = ['DDUUUUDD']

The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

'''

def count_valleys(steps, path):
    # transform path into ints ( 1 = up, -1 = down)
    path_int = [1 if char == 'U' else -1 for char in path]
    sea_level = 0
    below = False
    valleys = 0

    for step in path_int:
        # update sea level
        sea_level = sea_level + step
        # check if we're returning to sea level
        if sea_level >= 0 and below:
            valleys = valleys + 1
        
        # update below
        below = sea_level < 0

    return valleys

if __name__ == '__main__':
    print(count_valleys(8, 'UDDDUDUU'))