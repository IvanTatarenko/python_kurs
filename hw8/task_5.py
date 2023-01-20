def palindrom(word):
  if word == "".join(reversed(word)) :
    return True
  else:
    return False

if __name__ == "__main__":
  while(True):
    word = input('input: ')
    if word == '':
      break
    else:
      result = palindrom(word)
      if(result):
        print('Строка є паліндромом')
      else:
        print('Строка не є палідромом')