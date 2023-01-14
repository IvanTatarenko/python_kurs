def cell_rate(buy_rate):
  return round(buy_rate + (buy_rate * 0.05), 2)

#курс валют
AUH_BUY = {
    'EUR': 42.50,
    'USD': 50.00,
    'PLN': 30.00
}
AUH_CELL = {key : cell_rate(AUH_BUY[key]) for key in AUH_BUY}

#кількість купюр в касі
bank = {
  "USD": {
    100 : 90, 
    50: 20, 
    10: 10, 
    5:0, 
    1:0
  }
}

result_buy = {
  'currency': 'USD',
  'bank_sum': 0,
  'currency_value': 0.0,
  'auh_value': 0.0,
  'remain': 0.0,
  'offer_more': False,
  'amount_more': 0.0,
  'result_buy_more': 0.0,
  'offer_less': False,
  'enough_money': False
}
result_sell = {
  'currency': 'USD',
  'value': 0.00
}

#коеф. для підрахунку пропозиції купити більше або менше валюти
ALIQUIT_INDEX = 50
CLOSENESS_INTEREST = 0.05
closeness_index = ALIQUIT_INDEX * CLOSENESS_INTEREST

#Визначення - чи потрібно пропонувати взяти більше або менше
def offer():
  remain_currency = result_buy['remain'] / AUH_BUY[result_buy['currency']]
  if((remain_currency + result_buy['currency_value'] + closeness_index)//ALIQUIT_INDEX > result_buy['currency_value']//ALIQUIT_INDEX):
    result_buy['result_buy_more'] = (result_buy['currency_value']//ALIQUIT_INDEX + 1.0) * ALIQUIT_INDEX
    result_buy['amount_more'] = (result_buy['result_buy_more'] - result_buy['currency_value'])/AUH_BUY[result_buy['currency']]
    result_buy['offer_more'] = True
  elif((remain_currency + result_buy['currency_value'] - closeness_index)//ALIQUIT_INDEX < result_buy['currency_value']//ALIQUIT_INDEX):
    result_buy['offer_less'] = True
  
#Підрахунок грошей в касі
def bank_val():
  bank_sum = 0
  for i in bank[result_buy['currency']]:
    bank_sum += (i * bank[result_buy['currency']][i])
  result_buy['bank_sum'] = bank_sum
  if(result_buy['currency_value'] < bank_sum):
    result_buy['enough_money'] = True
  
#Вивід курсів валют
print(f"{'':*^17}")
print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
for i in AUH_BUY:
  print(f"*{AUH_BUY[i]:<6.2f}{i:^3}{AUH_CELL[i]:>6.2f}*")
print(f"{'':*^17}")

print(result_buy)

operation_selection = input("Ви бажаєте купити чи продати долари?(купити/продати)")

# купівля
def buy(currency):
  result_buy['auh_value'] = float(input(f"Введіть кількість гривень, яку ви хочете обміняти на {currency}: "))
  result_buy['currency_value'] = result_buy['auh_value'] // AUH_BUY[currency]
  result_buy['remain'] = result_buy['auh_value'] % AUH_BUY[currency]
  bank_val()
  if(result_buy['enough_money']):
    print(f"Ваша валюта {result_buy['currency_value']:>9.2f} {currency}")
    print(f"Ваша решта {result_buy['remain']:>10.2f} UAH")
    offer()
    if(result_buy['offer_more']):
      input_buy_more = input(f'Чи бажаете внести { result_buy["amount_more"] } грн щоб отримати рівно {result_buy["result_buy_more"]} дол?(Y/N):')
    elif(result_buy['offer_less']):
      pass
    else:
      print('Гарного дня!')
  # Не вситачає грошей
  else:
    input_buy = input(f'В обміннику не вистачає грошей. Можемо запропонувати {result_buy["bank_sum"]} {currency}?(Т/Н)')
    if input_buy == 'Y' or input_buy == 'y' or input_buy == 'Т' or input_buy == 'т':
      result_buy['remain'] = result_buy['auh_value'] - (result_buy["bank_sum"] / AUH_BUY[currency])
      print(f"Ваша валюта {result_buy['bank_sum']:>9.2f} {currency}")
      print(f"Ваша решта {result_buy['remain']:>10.2f} UAH")
    elif input_buy == 'N' or input_buy == 'n' or input_buy == 'Н' or input_buy == 'н':
      print('Гарного дня!')
    else:
      print('Помилка вводу')
  
  
# продаж
def sell(currency):
  value = float(input(f"Введіть кількість {currency}, яку ви хочете продати: "))
  result_sell['value'] = value *AUH_CELL[currency]

if operation_selection == 'купити' or operation_selection == 'regbnb':
  buy(result_buy['currency']) 
elif operation_selection == 'продати' or operation_selection == 'ghjlfnb':
  sell(result_sell['currency'])
  print(f"Ви отримуєте {result_sell['value']:>8.2f} грн")
else:
  print('Помилка вводу')




# def buy():
  
  


#     elif auto_index_more <= closeness_index:
#       result_buy_more = buy_calculations['result'] + auto_index_more + remain_usd
#       surcharge_amount = auto_index_more * AUH_BUY['USD']
#       input_buy_more = input(f'Чи бажаете внести { surcharge_amount } грн щоб отримати рівно {result_buy_more} дол?(Y/N):')
    
#       if input_buy_more == 'Y' or input_buy_more == 'y':
#         print(f'Внесіть суму до плати: { surcharge_amount } грн')
#         print(f"Ваша валюта {result_buy_more:.2f} дол")
#         print(f"Ваша решта 0 грн")
#       elif input_buy_more == 'N' or input_buy_more == 'n':
#         print(f"Ваша валюта {buy_calculations['result']:>9.2f} дол")
#         print(f"Ваша решта {remain:>10.2f} грн")
#       else:
#         print('Помилка вводу')
#     elif auto_index_less <= closeness_index: 
#       additional_buy = buy_calculations['result'] - auto_index_less
#       input_buy_less = input(f'Чи бажаєте купити рівно {additional_buy} дол?(Y/N):')
#       if input_buy_less == 'Y' or input_buy_less == 'y':
#         usd_remain = auto_index_less * AUH_BUY['USD'] + remain
#         print(f"Ваша валюта {additional_buy:>9.2f} дол")
#         print(f"Ваша решта {usd_remain:>10.2f} грн")
#       elif input_buy_less == 'N' or input_buy_less == 'n':
#         print(f"Ваша валюта {buy_calculations['result']:>9.2f} дол")
#         print(f"Ваша решта {remain:>10.2f} грн")
#       else:
#         print('Помилка вводу')
#   else:
#     print("Недостатньо грошей в касі")
  
  







