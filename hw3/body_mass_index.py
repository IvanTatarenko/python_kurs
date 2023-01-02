input_mass = input(f'Яка ваша маса тіла(kg/lb)?')
if input_mass.endswith('kg'):
  body_mass = float(input_mass[:-2])
elif input_mass.endswith('lb'):
  body_mass = float(input_mass[:-2]) * 0.45359237
else:
  print('Помилка вводу')

input_height = input(f'Який ваш зріст(cm/m/ft)?')
if input_height.endswith('cm'):
  height = float(input_height[:-2]) / 100
elif input_height.endswith('m'):
  height = float(input_height[:-1])
elif input_height.endswith('ft'):
  height = float(input_height[:-2]) * 0.3048
else:
  print('Помилка вводу')

mass_index = body_mass / height**2

print(f'Ваш коефіцієнт маси тіла - {mass_index:.1f}')