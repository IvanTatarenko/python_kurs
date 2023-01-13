def cell_rate(buy_rate):
  return round(buy_rate + (buy_rate * 0.05), 2)

#курс валют
AUH_BUY = {
    "EUR": 42.50,
    "USD": 50.00,
    "PLN": 30.00
}
AUH_CELL = {
    "EUR": cell_rate(AUH_BUY['EUR']),
    "USD": cell_rate(AUH_BUY['USD']),
    "PLN": cell_rate(AUH_BUY['PLN'])
}


#коеф. для підрахунку пропозиції купити більше або менше валюти
ALIQUIT_INDEX = 50
CLOSENESS_INTEREST = 0.05
closeness_index = ALIQUIT_INDEX * CLOSENESS_INTEREST

buy_calculations = {
}
#Вивід курсів валют
print(f"{'':*^17}")
print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
for i in AUH_BUY:
  print(f"*{AUH_BUY[i]:<6.2f}{i:^3}{AUH_CELL[i]:>6.2f}*")
print(f"{'':*^17}")

operation_selection = input("Ви бажаєте купити чи продати долари?(купити/продати)")

def buy():
  buy_calculations['value'] = float(input("Введіть кількість гривень, яку ви хочете продати: "))
  buy_calculations['result'] = buy_calculations['value'] // AUH_BUY['USD']
  print(buy_calculations)
  remain = buy_calculations['value'] % AUH_BUY['USD']
  print(f"Ваша валюта {buy_calculations['result']:>9.2f} дол")
  print(f"Ваша решта {remain:>10.2f} грн")
  
  remain_usd = remain / AUH_BUY['USD']
  auto_index_more = ALIQUIT_INDEX - (buy_calculations['result'] % ALIQUIT_INDEX) - remain_usd
  auto_index_less = buy_calculations['result'] % ALIQUIT_INDEX

  if buy_calculations['result'] % ALIQUIT_INDEX == 0:
    print('Гарного дня!')
  elif auto_index_more <= closeness_index:
    result_buy_more = buy_calculations['result'] + auto_index_more + remain_usd
    surcharge_amount = auto_index_more * AUH_BUY['USD']
    input_buy_more = input(f'Чи бажаете внести { surcharge_amount } грн щоб отримати рівно {result_buy_more} дол?(Y/N):')
    
    if input_buy_more == 'Y' or input_buy_more == 'y':
      print(f'Внесіть суму до плати: { surcharge_amount } грн')
      print(f"Ваша валюта {result_buy_more:.2f} дол")
      print(f"Ваша решта 0 грн")
    elif input_buy_more == 'N' or input_buy_more == 'n':
      print(f"Ваша валюта {buy_calculations['result']:>9.2f} дол")
      print(f"Ваша решта {remain:>10.2f} грн")
    else:
      print('Помилка вводу')
  elif auto_index_less <= closeness_index: 
    additional_buy = buy_calculations['result'] - auto_index_less
    input_buy_less = input(f'Чи бажаєте купити рівно {additional_buy} дол?(Y/N):')
    if input_buy_less == 'Y' or input_buy_less == 'y':
      usd_remain = auto_index_less * AUH_BUY['USD'] + remain
      print(f"Ваша валюта {additional_buy:>9.2f} дол")
      print(f"Ваша решта {usd_remain:>10.2f} грн")
    elif input_buy_less == 'N' or input_buy_less == 'n':
      print(f"Ваша валюта {buy_calculations['result']:>9.2f} дол")
      print(f"Ваша решта {remain:>10.2f} грн")
    else:
      print('Помилка вводу')

if operation_selection == 'купити' or operation_selection == 'regbnb':
  buy()
  # value = float(input("Введіть кількість гривень, яку ви хочете продати: "))
  # result = value // AUH_BUY['USD']
  # remain = value % AUH_BUY['USD']
  # print(f"Ваша валюта {result:>9.2f} дол")
  # print(f"Ваша решта {remain:>10.2f} грн")
  
  # remain_usd = remain / AUH_BUY['USD']
  # auto_index_more = ALIQUIT_INDEX - (result % ALIQUIT_INDEX) - remain_usd
  # auto_index_less = result % ALIQUIT_INDEX

  # if result % ALIQUIT_INDEX == 0:
  #   print('Гарного дня!')
  # elif auto_index_more <= closeness_index:
  #   result_buy_more = result + auto_index_more + remain_usd
  #   surcharge_amount = auto_index_more * AUH_BUY['USD']
  #   input_buy_more = input(f'Чи бажаете внести { surcharge_amount } грн щоб отримати рівно {result_buy_more} дол?(Y/N):')
    
  #   if input_buy_more == 'Y' or input_buy_more == 'y':
  #     print(f'Внесіть суму до плати: { surcharge_amount } грн')
  #     print(f"Ваша валюта {result_buy_more:.2f} дол")
  #     print(f"Ваша решта 0 грн")
  #   elif input_buy_more == 'N' or input_buy_more == 'n':
  #     print(f"Ваша валюта {result:>9.2f} дол")
  #     print(f"Ваша решта {remain:>10.2f} грн")
  #   else:
  #     print('Помилка вводу')
  # elif auto_index_less <= closeness_index: 
  #   input_buy_less = input(f'Чи бажаєте купити рівно {result - (auto_index_less)} дол?(Y/N):')
  #   if input_buy_less == 'Y' or input_buy_less == 'y':
  #     usd_remain = auto_index_less * AUH_BUY['USD'] + remain
  #     print(f"Ваша валюта {result - auto_index_less:>9.2f} дол")
  #     print(f"Ваша решта {usd_remain:>10.2f} грн")
  #   elif input_buy_less == 'N' or input_buy_less == 'n':
  #     print(f"Ваша валюта {result:>9.2f} дол")
  #     print(f"Ваша решта {remain:>10.2f} грн")
  #   else:
  #     print('Помилка вводу')

  
elif operation_selection == 'продати' or operation_selection == 'ghjlfnb':
  value = float(input("Введіть кількість доларів, яку ви хочете продати: "))
  result = value * AUH_CELL['USD']
  print(f"Ви отримуєте {result:>8.2f} грн")
else:
  print('Помилка вводу')





