input_int = int(input('Введіть число від 6 до 16: '))

multiplier_a = input_int - 4
multiplier_b = input_int + 3

if (6 <= input_int and input_int <= 16):
  while(multiplier_a <= multiplier_b):
    print(f'{multiplier_a} * {input_int} = {input_int*multiplier_a}')
    multiplier_a +=1
else: print('Невірне число')