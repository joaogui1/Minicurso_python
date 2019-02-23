import pdb

def square(x):
    return x*x

pdb.set_trace()
x = 432

x += x

l = list(range(12))


square(x)

for num in l:
    x = x/(11 - num)
