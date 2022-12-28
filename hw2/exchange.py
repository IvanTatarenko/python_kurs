AUH_EUR_BUY = 42.50
AUH_USD_BUY = 40.53
AUH_PLN_BUY = 30.00
AUH_EUR_CELL = round(AUH_EUR_BUY + (AUH_EUR_BUY * 0.05), 2)
AUH_USD_CELL = round(AUH_USD_BUY + (AUH_USD_BUY * 0.05), 2)
AUH_PLN_CEll = round(AUH_PLN_BUY + (AUH_PLN_BUY * 0.05), 2)
ALIQUIT_INDEX = 50
CLOSENESS_INDEX = 5

#Вивід курсів валют
print(f"{'':*^17}")
print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
print(f"*{AUH_EUR_BUY:<6.2f}{'EUR':^3}{AUH_EUR_CELL:>6.2f}*")
print(f"*{AUH_USD_BUY:<6.2f}{'USD':^3}{AUH_USD_CELL:>6.2f}*")
print(f"*{AUH_PLN_BUY:<6.2f}{'PLN':^3}{AUH_PLN_CEll:>6.2f}*")
print(f"{'':*^17}")

operation_selection = input("Ви бажаєте купити чи продати долари?(купити/продати)")

if operation_selection == 'купити':
  value = float(input("Введіть кількість гривень, яку ви хочете продати: "))
  result = value // AUH_USD_BUY
  remain = value % AUH_USD_BUY
  print(f"Вашаша валюти {result:.2f} дол")
  print(f"Ваша решта {remain:>8.2f} грн")
  
elif operation_selection == 'продати':
  value = float(input("Введіть кількість доларів, яку ви хочете продати: "))
  result = value * AUH_USD_CELL
  print(f"Ви отримуєте {result:>8.2f} грн")
else:
  print('Помилка вводу')





