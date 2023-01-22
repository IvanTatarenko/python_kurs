def brackets(string):
  stack = []
  for char in string:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0  
            
if __name__ == "__main__":
  assert brackets("())")==False
  assert brackets("())(")==False
  assert brackets("(s(sss)sssssssssssssssssssssssssss)")==True