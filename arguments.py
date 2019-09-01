# args lets you pass a variable number of arguments to a function

def suma(*args):
    res = 0
    for i in args:
        res += i
    return res

#kwargs lets you pass multiple keyword arguments
def titles(**kwargs):
    for person, title in kwargs.items():
        print(f'{person} {title}')


# print(suma(1.0, 2.5, 3, 4))
# titles(Gallahad="The Pure", Robin="The Brave")

inputs = [4, 3, 2, 1]

def f(a, b, c, d):
    return a**2 + b**3 + c**4 + d**5

def sum_sq(a, b):
    return(a*a + b*b)

print(f(*inputs))
