AUH_EUR_BUY = 42.00
AUH_USD_BUY = 40.00
AUH_PLN_BUY = 30.00
AUH_EUR_CELL = AUH_EUR_BUY + (AUH_EUR_BUY * 0.05)
AUH_USD_CELL = AUH_USD_BUY + (AUH_USD_BUY * 0.05)
AUH_PLN_CEll = AUH_PLN_BUY + (AUH_PLN_BUY * 0.05)

print(f"{'':*^15}")
print(f"{'*BUY':<5}{'':5}{'SELL*':>5}")
print(f"*{AUH_EUR_BUY:<5}{'EUR':^3}{AUH_EUR_CELL:>5}*")
print(f"*{AUH_USD_BUY:<5}{'USD':^3}{AUH_USD_CELL:>5}*")
print(f"*{AUH_PLN_BUY:<5}{'PLN':^3}{AUH_PLN_CEll:>5}*")
print(f"{'':*^15}")

val_uah = float(input("Введіть кількість гривень, яку ви хочете продати: "))
result = val_uah // AUH_USD_BUY
remain = val_uah % AUH_USD_BUY

print(f"Вашаша валюти {result} дол")
print(f"Ваша решта {remain:>7} грн")

