""" def ranger (*args, **kwargs):
    lst = []
    
    lower_bound, upper_bound = args

    ticker = lower_bound

    while ticker<=upper_bound:
        lst.append(ticker)
        ticker+=1
    
    print(lst)

a = ranger(9, 10)
print(a) """

numbers = ['one', 'two', 'three']

print(numbers[0], numbers[1], numbers[2])
print(*numbers)
