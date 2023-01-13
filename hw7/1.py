start = int(input('Введіть число a: '))
end = int(input('Введіть число b: '))

dividible_at = [2, 3, 4, 5, 6]
if (1 <= start and start < 200 and end <= 200 and end > 1):
  dividible = {2: [], 3: [], 4: [], 5: [], 6: []}
  dividible = {key : [] for key in dividible_at}
  
  for i in dividible_at:
    for j in range(start+1, end):
      if(j % i == 0):
        dividible[i].append(j)
  
  print(dividible)
  for i in dividible:
    print(f'Dividible by {i}: {dividible[i][:10]}')
else: print('Невірні числа')