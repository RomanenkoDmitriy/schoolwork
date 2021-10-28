def fibanachi(stop, arr=[], fib=0, item=1):
    arr.append(fib)
    fib +=item
    item = fib - item
    if fib < stop:
        return fibanachi(stop, arr, fib, item)
    return arr


stop = 20
print(fibanachi(stop))
