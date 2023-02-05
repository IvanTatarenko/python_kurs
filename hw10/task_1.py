def flatten(array):
    output = []
    for item in array:
        if isinstance(item, (list, tuple)):
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

assert flatten([1,[2], [3,[6]]]) == [1, 2, 3, 6]
assert flatten([[[[]]]]) == []