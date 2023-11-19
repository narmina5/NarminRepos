# TASKS (DAY 4):
# 01
def add(x, y):
    return x + y


# 02
def multiply(x, y):
    return x * y


# 03
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# 04
def find_max(given_list):
    if not given_list:
        raise ValueError("List is empty")
    return max(given_list)
