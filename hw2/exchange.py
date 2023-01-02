#курс валют
AUH_EUR_BUY = 42.50
AUH_USD_BUY = 50.00
AUH_PLN_BUY = 30.00
AUH_EUR_CELL = round(AUH_EUR_BUY + (AUH_EUR_BUY * 0.05), 2)
AUH_USD_CELL = round(AUH_USD_BUY + (AUH_USD_BUY * 0.05), 2)
AUH_PLN_CEll = round(AUH_PLN_BUY + (AUH_PLN_BUY * 0.05), 2)

ALIQUIT_INDEX = 50
CLOSENESS_INTEREST = 0.05
closeness_index = ALIQUIT_INDEX * CLOSENESS_INTEREST

#Вивід курсів валют
print(f"{'':*^17}")
print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
print(f"*{AUH_EUR_BUY:<6.2f}{'EUR':^3}{AUH_EUR_CELL:>6.2f}*")
print(f"*{AUH_USD_BUY:<6.2f}{'USD':^3}{AUH_USD_CELL:>6.2f}*")
print(f"*{AUH_PLN_BUY:<6.2f}{'PLN':^3}{AUH_PLN_CEll:>6.2f}*")
print(f"{'':*^17}")

operation_selection = input("Ви бажаєте купити чи продати долари?(купити/продати)")

if operation_selection == 'купити' or operation_selection == 'regbnb':
  value = float(input("Введіть кількість гривень, яку ви хочете продати: "))
  result = value // AUH_USD_BUY
  remain = value % AUH_USD_BUY
  print(f"Ваша валюта {result:>9.2f} дол")
  print(f"Ваша решта {remain:>10.2f} грн")
  
  remain_usd = remain / AUH_USD_BUY
  auto_index_more = ALIQUIT_INDEX - (result % ALIQUIT_INDEX) - remain_usd
  auto_index_less = result % ALIQUIT_INDEX

  if result % ALIQUIT_INDEX == 0:
    print('Гарного дня!')
  elif auto_index_more <= closeness_index:
    result_buy_more = result + auto_index_more + remain_usd
    input_buy_more = input(f'Чи бажаете внести { auto_index_more * AUH_USD_BUY } грн щоб отримати рівно {result_buy_more} дол?(Y/N):')
    
    if input_buy_more == 'Y' or input_buy_more == 'y':
      print(f'Внесіть суму до плати: { auto_index_more * AUH_USD_BUY } грн')
      print(f"Ваша валюта {result_buy_more:.2f} дол")
      print(f"Ваша решта 0 грн")
    elif input_buy_more == 'N' or input_buy_more == 'n':
      print(f"Ваша валюта {result:>9.2f} дол")
      print(f"Ваша решта {remain:>10.2f} грн")
    else:
      print('Помилка вводу')
  elif auto_index_less <= closeness_index: 
    input_buy_less = input(f'Чи бажаєте купити рівно {result - (auto_index_less)} дол?(Y/N):')
    if input_buy_less == 'Y' or input_buy_less == 'y':
      print(f"Ваша валюта {result - (auto_index_less):>9.2f} дол")
      print(f"Ваша решта {auto_index_less * AUH_USD_BUY + remain:>10.2f} грн")
    elif input_buy_less == 'N' or input_buy_less == 'n':
      print(f"Ваша валюта {result:>9.2f} дол")
      print(f"Ваша решта {remain:>10.2f} грн")
    else:
      print('Помилка вводу')

  
elif operation_selection == 'продати' or operation_selection == 'ghjlfnb':
  value = float(input("Введіть кількість доларів, яку ви хочете продати: "))
  result = value * AUH_USD_CELL
  print(f"Ви отримуєте {result:>8.2f} грн")
else:
  print('Помилка вводу')





