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
  },
  "UAH": {
    1000: 5,
    500: 10,
    200: 50,
    100 : 90, 
    50: 20, 
    10: 10, 
    5:0, 
    1:0
  },
  
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
  'remain_less': 0.0,
  'result_buy_less': 0.0,
  'enough_money': False,
  'bills_ok': True
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
    result_buy['amount_more'] = ((result_buy['result_buy_more'] - result_buy['currency_value'])*AUH_BUY[result_buy['currency']])-result_buy['remain']
    result_buy['offer_more'] = True
  elif((remain_currency + result_buy['currency_value'] - closeness_index)//ALIQUIT_INDEX < result_buy['currency_value']//ALIQUIT_INDEX and result_buy['currency_value'] % ALIQUIT_INDEX != 0):
    result_buy["result_buy_less"] = ((remain_currency + result_buy['currency_value'])//ALIQUIT_INDEX)*AUH_BUY[result_buy['currency']]
    result_buy['remain_less'] = result_buy['remain'] + ((result_buy['currency_value'] - result_buy["result_buy_less"]) * AUH_BUY[result_buy['currency']])
    if((remain_currency + result_buy['currency_value'])//ALIQUIT_INDEX) == 0.0:
      result_buy['offer_less'] = False
    else:
      result_buy['offer_less'] = True
    
    
  
# Підрахунок грошей в касі
def bank_val(currency):
  bank_sum = 0
  for i in bank[currency]:
    bank_sum += (i * bank[currency][i])
  result_buy['bank_sum'] = bank_sum
  if(result_buy['currency_value'] <= bank_sum):
    result_buy['enough_money'] = True
 

# Перевірка наявності потрібних купюр в касі
def count_bills(currency):
  res = result_buy['currency_value']
  for i in bank[currency]:
    bills = bank[currency][i]
    while (bills > 0 and res > 0):
      res -= i
      if(res < 0):
        res += i
        break
      bills -= 1
  if(res > 0):
    result_buy['bills_ok'] = False
  else:
    result_buy['bills_ok'] = True
  
  



# Вивід курсів валют
print(f"{'':*^17}")
print(f"*{'BUY':^5}{'':5}{'SELL':^5}*")
for i in AUH_BUY:
  print(f"*{AUH_BUY[i]:<6.2f}{i:^3}{AUH_CELL[i]:>6.2f}*")
print(f"{'':*^17}")



operation_selection = input("Ви бажаєте купити чи продати долари?(купити/продати)")

# купівля
def buy(currency):
  result_buy['auh_value'] = float(input(f"Введіть кількість гривень, яку ви хочете обміняти на {currency}: "))
  result_buy['currency_value'] = result_buy['auh_value'] // AUH_BUY[currency]
  result_buy['remain'] = result_buy['auh_value'] % AUH_BUY[currency]
  bank_val(result_buy['currency'])
  if(result_buy['enough_money']):
    count_bills(result_buy['currency'])
    if(result_buy['bills_ok']):
      print(f"Ваша валюта {result_buy['currency_value']:>9.2f} {currency}")
      print(f"Ваша решта {result_buy['remain']:>10.2f} UAH")
      offer()
      if(result_buy['offer_more']):
        input_buy_more = input(f'Чи бажаете внести { result_buy["amount_more"] } грн щоб отримати рівно {result_buy["result_buy_more"]} дол?(Т/Н):')
        if(input_buy_more == 'Y' or input_buy_more == 'y' or input_buy_more == 'Т' or input_buy_more == 'т'):
          print(f'Внесіть суму до плати: { result_buy["amount_more"] } грн')
          count_bills(result_buy['currency'])
          if(result_buy['bills_ok']):
            print(f"Ваша валюта {result_buy['result_buy_more']:>9.2f} {currency}")
            print(f"Ваша решта {0.00:>10.2f} UAH")
          else:
            print(f'Відстуні підходящі купюри {currency} в касі:(')
        elif(input_buy_more == 'N' or input_buy_more == 'n' or input_buy_more == 'Н' or input_buy_more == 'н'):
          print(f"Ваша валюта {result_buy['currency_value']:>9.2f} {currency}")
          print(f"Ваша решта {result_buy['remain']:>10.2f} UAH")
        else:
          print('Помилка вводу')
        
      elif(result_buy['offer_less']):
        input_buy_less = input(f'Чи бажаєте купити рівно {result_buy["result_buy_less"]} USD?(Т/Н):')
        if(input_buy_less == 'Y' or input_buy_less == 'y' or input_buy_less == 'Т' or input_buy_less == 'т'):
          count_bills(result_buy['currency'])
          if(result_buy['bills_ok']):
            print(f"Ваша валюта {result_buy['result_buy_less']:>9.2f} {currency}")
            print(f"Ваша решта {result_buy['remain_less']:>10.2f} UAH")
          else:
            print(f'Відстуні підходящі купюри {currency} в касі:(')
        elif(input_buy_less == 'N' or input_buy_less == 'n' or input_buy_less == 'Н' or input_buy_less == 'н'):
          print(f"Ваша валюта {result_buy['currency_value']:>9.2f} {currency}")
          print(f"Ваша решта {result_buy['remain']:>10.2f} UAH")
        else:
          print('Помилка вводу')
      
      else:
        print('Гарного дня!')
    else:
      print(f'Відстуні підходящі купюри {currency} в касі:(')
    
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
  result_buy['currency_value'] = value *AUH_CELL[currency]
  bank_val('UAH')
  if(result_buy['enough_money']):
    print(f"Ви отримуєте {result_buy['currency_value']:>8.2f} грн")
  else:
    input_buy = input(f'В обміннику не вистачає грошей. Можемо запропонувати {result_buy["bank_sum"]} UAH?(Т/Н)')
    if input_buy == 'Y' or input_buy == 'y' or input_buy == 'Т' or input_buy == 'т':
      result_buy['remain'] = (result_buy['currency_value'] - result_buy['bank_sum']) / AUH_CELL[currency]
      print(f"Ви отримуєте {result_buy['bank_sum']:>8.2f} UAH")
      print(f"Ваша решта {result_buy['remain']:>10.2f} USD")
    elif input_buy == 'N' or input_buy == 'n' or input_buy == 'Н' or input_buy == 'н':
      print('Гарного дня!')
    else:
      print('Помилка вводу')
  

if operation_selection == 'купити' or operation_selection == 'regbnb':
  buy(result_buy['currency']) 
elif operation_selection == 'продати' or operation_selection == 'ghjlfnb':
  sell(result_sell['currency'])
  
else:
  print('Помилка вводу')




  







