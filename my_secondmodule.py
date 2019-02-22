def f():
    return 9
def g(n):
    fib = [1, 1]
    while(n > 0):
        fib = [fib[1], fib[0] + fib[1]]
        n -= 1
    return fib[0]
