def join_ints(my_list):
  result = ''
  for i in my_list:
    if (type(i) == int):
      result += str(i)
  return(int(result))

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143
