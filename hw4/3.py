a = int(input('Введіть число a: '))
b = int(input('Введіть число b: '))
if (1 <= a and a < 200 and b <= 200 and b > 1):
  dividible_2 = []
  dividible_3 = []
  dividible_4 = []
  dividible_5 = []
  dividible_6 = []
  c = a
  while (c < b - 1):
    c += 1
    if(c % 2 == 0): dividible_2.append(c)
    if(c % 3 == 0): dividible_3.append(c)
    if(c % 4 == 0): dividible_4.append(c)
    if(c % 5 == 0): dividible_5.append(c)
    if(c % 6 == 0): dividible_6.append(c)
  print(f'Dividible by 2: {dividible_2[:10]}')
  print(f'Dividible by 3: {dividible_3[:10]}')
  print(f'Dividible by 4: {dividible_4[:10]}')
  print(f'Dividible by 5: {dividible_5[:10]}')
  print(f'Dividible by 6: {dividible_6[:10]}')
else: print('Невірні числа')


