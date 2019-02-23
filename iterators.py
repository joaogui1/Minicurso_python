nums = [1, 2, 3, 4]

#iterables have the __iter__ method, that returns an iterator

# print(dir(nums))

#iterables have the __next__ method

# print(dir(nums))

class MyRange:
    def __init__(self, start, step, end):
        self.value = start
        self.step = step
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value + self.step > self.end:
            raise StopIteration
        current = self.value
        self.value += self.step
        return current

nums = MyRange(0, 2, 12)

for i in nums:
    print(i)
