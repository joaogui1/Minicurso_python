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


print(suma(1, 2, 3, 4))
titles(Gallahad="The Pure", Robin="The Brave")

inputs = {'a':3, 'b':4}

def sum_sq(a, b):
    return(a*a + b*b)

print(sum_sq(**inputs))
