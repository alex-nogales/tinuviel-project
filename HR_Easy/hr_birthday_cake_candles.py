'''
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
''' 

candles = [5, 5, 5, 5]

def birthday_cake_candles(candles):
    max_heigh = max(candles)
    counter = 0
    for candle in candles:
        if candle == max_heigh:
            counter += 1
    return counter


if __name__ == '__main__':
    print(birthday_cake_candles(candles))