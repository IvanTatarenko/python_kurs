text_sum = 0
text = ''
while (text != 'end'):
  text = input('Введіть число: ')
  if (text.isdecimal()): text_sum += int(text)
  else: print('Нправильний символ. Вводьте тільки числа')

print(f'Сума чисел: {text_sum}')