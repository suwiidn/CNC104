#6809658138
def get_most_recent(numbers_in_order, numbers_to_test):

    n = len(numbers_in_order)
    for i in range(n - 1, -1, -1):

        if i in numbers_to_test:

            return i

    return -1

print("1.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [2, 0, 3]))
print("2.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [0, 7, 2]))
print("3.", get_most_recent([0, 1, 2, 8, 9, 0, 3, 4, 6], [1, 9, 2, 8]))
print("4.", get_most_recent([4, 1, 4, 5, 4, 1], [0, 7, 3]))
print("5.", get_most_recent([8, 1, 2, 0, 8, 4, 1], [8, 7, 3]))
print("6.", get_most_recent([], [8, 1, 0, 3]))

numbers_in_order = [1, 1, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0, 3, 4, 1, 2, 4, 0, 3, 8, 8, 5, 5]
print("7.", get_most_recent(numbers_in_order, [1, 0, 3, 4]))

numbers_in_order = [1, 2, 2, 2, 2, 3, 1, 3, 8, 0]
print("8.", get_most_recent(numbers_in_order, [1, 8, 2, 3, 4, 2]))