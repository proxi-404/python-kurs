def fib(n):
    if (n == 0): return 0
    elif (n == 1): return 1
    else:
        result = 0
        i = 2
        last = 1
        penultimate = 0
        while (i <= n):
            result = last + penultimate
            penultimate = last
            last = result
            i += 1
    return result
    
for j in range(100):
    for i in range(1000):
        print(fib(i),end=", ")
        fib(i)
print()
