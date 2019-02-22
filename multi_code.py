import my_module
from my_secondmodule import g

my_module.f()
print(g(10))

try:
    fib_index = int(input())
except ValueError: #Exception
    print("Not a Number")
else:
    print(g(fib_index))
finally:
    print("I always run! :)")
