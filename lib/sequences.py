#!/usr/bin/env python3
fib_series = [0, 1]
def print_fibonacci(length):
    if length==0:
        print([])
    elif length==1:
        print([0])
    elif length==2:
        print([0,1])
    else:
         
        for i in range(2, length):
            fib_series.append(fib_series[-1] + fib_series[-2])
        print(fib_series)