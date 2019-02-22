import pdb

def square(x):
    return x*x

x = 432

x += x

l = list(range(12))

pdb.set_trace()

square(x)

for num in l:
    x = x/(11 - num)
