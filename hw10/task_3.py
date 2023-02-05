def roman_arabic(string): 
  rom_val = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
  arabic = 0
  for i in range(len(string)): 
    if i > 0 and rom_val[string[i]] > rom_val[string[i-1]]: 
      arabic += rom_val[string[i]] - 2 * rom_val[string[i-1]] 
    else: 
      arabic += rom_val[string[i]] 
  return arabic 

if __name__ == "__main__":
  assert roman_arabic("I")==1
  assert roman_arabic("II")==2
  assert roman_arabic("III")==3
  assert roman_arabic("IV")==4
  assert roman_arabic("V")==5
  assert roman_arabic("VI")==6
  assert roman_arabic("VII")==7
  assert roman_arabic("VIII")==8
  assert roman_arabic("IX")==9
  assert roman_arabic("X")==10
  assert roman_arabic("XI")==11
  assert roman_arabic("DC")==600
  assert roman_arabic("MC")==1100
  assert roman_arabic("MDCIV")==1604