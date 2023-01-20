if __name__ == "__main__":
  result = 0
  while(True):
    num = input('Введіть число: ')
    if(num.isdigit()):
      if(int(num)%2 == 0):
        result += int(num)
      else:
        result -= int(num)
    elif(num == 'end'):
      print(f'Сума чисел: {result}')
      break
    else:
      print('Невірний ввід')
      continue