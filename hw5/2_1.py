def second_smallest(array):
    return(sorted(array)[1])

assert second_smallest([1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1