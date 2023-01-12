def turn(number):
  res = 0
  while(number > 0):
    a = number % 10
    number = number // 10
    res = res * 10
    res = res + a
  return(res)


def join_ints(my_list):
  result = []
  res = 0

  for i in my_list:
    if (type(i) == int):
      result.append(i)
  
  for i in range(len(result)):
    res += (10**i) * result[i]

  return(turn(res))

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143



