

def stock_picker(arr):
    profit = -1
    lowest = arr[0]
    for i in range(1, len(arr)):
        if lowest > arr[i]:
            lowest = arr[i]
        else:
            temp = arr[i] - lowest
            if temp > profit:
                profit = temp
    return profit

