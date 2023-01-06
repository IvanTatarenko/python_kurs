input_int = int(input('Введіть число від 1 до 100: '))
multiplier = 1
if (1 <= input_int and input_int <= 100):
  while(multiplier < 9):
    print(f'{multiplier} * {input_int} = {input_int*multiplier}')
    multiplier +=1
else: print('Невірне число')