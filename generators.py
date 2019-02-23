
#iterator function
def squares(nums):
    for i in nums:
        yield (i*i)

small_squares = squares([1, 2, 3, 4, 5])

small_squares = (x*x for x in [1, 2, 3, 4, 5])

# for sq in small_squares:
#     print(sq)
#
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

fib_seq = fib(10)

for i in fib_seq:
    print(i)
