def list_intercection(list1, list2):
    result = list(set(list1) & set(list2))
    if (len(result) > 0):
      return(result)
    else:
      return(None)

assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1, ]
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]