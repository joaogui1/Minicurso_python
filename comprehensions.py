'''Corey's Schafer tutorial without answers'''


nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums


# I want 'n*n' for each 'n' in nums


# I want 'n' for each 'n' in nums if 'n' is even
# lista = [n for n in nums if n%2 == 0]

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))
# print(lista)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# If name not equal to Peter

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print i
