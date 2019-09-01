'''Tribonnacci
    input: int n
    output: print the nth Tribonnacci number
>>> tribonnacci(0)
1

>>> tribonnacci(5)
9

>>> [tribonnacci(n) for n in range(6)]
[1, 1, 1, 3, 5, 9]
'''

def tribonnacci(n):
    if n < 3:
        return 1
    return tribonnacci(n - 1) + tribonnacci(n - 2) + tribonnacci(n - 3)
 #python -m doctest Trib.py
