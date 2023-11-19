# TASKS (DAY eShopper): (map, filter, reduce and labmda)
from functools import reduce

# 01
n = 5
m = 10

odds = list(filter(lambda x: x % 2 != 0, range(n, m + 1)))
print(odds)

# or
t = 20
s = 30

evens = list(filter(lambda x: x % 2 == 0, range(t, s + 1)))
print(evens)

# 02
a = map(lambda x: x ** 2, range(5, 11))
print(list(a))

# 03
n = 1
m = 50

my_list = list(range(n, m + 1))

even_pairs = filter(lambda x: x % 2 == 0, my_list)

squared_even_pairs = list(map(lambda x: x ** 2, even_pairs))

print(squared_even_pairs)

# 04
my_list = [1, 3, 6, 7, 13]
result = reduce(lambda x, y: x + y, my_list)

print(result)

# 05
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = ["John", "Jane", "Jack", "Jill", "Joe", "Jenny", "Jen", "Jenna", "Jenifer", "Jeniffer"]

x = list(zip(my_list, my_list2))

print(x)


# TASKS (DAY eShopper):

# 01
a = 10
b = 20
largest = max(a, b, key=lambda x: x)

print(largest)

# 02
my_list = list(range(1, 11))

even_pairs = filter(lambda x: x % 2 == 0, my_list)

squared_even_pairs = list(map(lambda x: x ** 2, even_pairs))

print(squared_even_pairs)

# 03
L1 = [8, -3, 2]
L2 = [3, 7, 5]
L3 = [4, 8, 1]

result = list(map(lambda x, y, z: x + y + z, L1, L2, L3))

print(result)

# 04


def filter_positive_numbers(numbers):
    positive_nums = list(filter(lambda x: x > 0, numbers))
    return positive_nums


my_list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

positive_numbers = filter_positive_numbers(my_list)

print(positive_numbers)

