"""
int a;
float b;
string c;
"""
"""
aljakdajdskjaskdajd
"""
"""
integer - int - ціле число
float - флоат - дробні числа
strint - строки
"""
a = 5
d = 8
b = 3.1# 3 + 1/10 2**63 - 1 -> 10**18

a = -3
c = a * 3
print(a)
#print(a/3, type(a/3))# при діленні цілі на цілі ми отримуємо флоат.
print(d // a, d % a)#
#print(d/a) -3 + 0.34
"""
Увага, засідка!
a - чисельник цілочисельного ділення. 
n - знаменик цілочисельного ділення.
8 % -3
a = 8
n = -3
floor - округлення
r = a- (n*floor(a/n))
r = 8 - (-3* 3)=1
java_script = 8 - (-3*2)= 8 - 6 = 2
2
"""
# import math
# a = 8
# n = -3
# r = a - (n * math.floor(a/n))
# print(r)
#s = "s"
# print(2**10)
# print(1.4e10)
#print(0.1*3 == 0.3)
#import decimal
#print(2/0)


"""
val_1 = 3
num_apples = 5
numApples = 5
Змінні мають починатись з малої літери!
"""
#my_str = "d"#ascii, unicode
#my_str_2 = "sa"

#print(my_str_2+5)
#print(my_str_2 + str(a))#
#print(int("5"), float("5.1"), float(5))
#print(f"змінна а дорівнює {a}")
#some_line = "Hello Word"
#print(some_line)

import math
#print(f"the aprox {math.pi:10.3f}")
a = 10000000
b = 100
c = 1000

print(f"{a:10} {b:*^10} {c:10}")
print(f"{c:10} {a:10} {b:10}")
print(f"{c:<10} {a:10} {b:>10}")




