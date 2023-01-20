def sum_list(array):
    res = sum(float(i) for i in array)
    if res % 1 == 0:
        return int(res)
    return res

if __name__ == "__main__":
  assert sum_list([1, 2, "1"]) == 4
  assert type(sum_list([1, 2, "1"])) == int
  assert sum_list([1, 2, "1", "1.1"]) == 5.1
  assert type(sum_list([1, 2, "1", "1.1"])) == float
  assert sum_list([1, 2, "1", "-1.0"]) == 3
  assert type(sum_list([1, 2, "1", "-1.0"])) == int
  
  


