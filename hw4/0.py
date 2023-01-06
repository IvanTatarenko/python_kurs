password = input('Введіть пароль ')

counts = 0
letter_big = False
letter_small = False
letter_number = False
letter_special = False

for i in password:
  counts += 1
  if (i.isupper() == True): letter_big = True
  if (i.islower() == True): letter_small = True
  if (i.isnumeric() == True): letter_number = True
  if (i.isnumeric() == False and  i.isalpha() == False): letter_special = True

if (counts >= 12 and letter_big == True and letter_small == True and letter_number == True and letter_special == True):
  print('Пароль прийнято')
else:
  if (counts < 12): print('Занадто мало символів, введіть більше 12 символів')
  if (letter_big == False): print('Відстутні великі літери')
  if (letter_small == False): print('Відстутні малі літери')
  if (letter_number == False): print('Відстутні цифри')
  if (letter_special == False): print('Відстутні спец символи')




