"""
складати і скорочуавти раціональні дроби . 
"""
def reduction(a, b):
  while a % b != 0:
    a, b = b, a % b
  return b

def divide(a, b):
  if(a[1] != b[1]):
    return None
  c = (a[0]+b[0])
  d = a[1]
  e = reduction(c, d)
  return (c//3, d//e)

if __name__ == "__main__":
  assert divide((1, 8), (3, 8)) == (1, 2)#1\8 + 3\8 = 4\8 = 1\2
  assert divide((1, 0), (3, 8)) == None#1\0 + 3\8 - not valid

