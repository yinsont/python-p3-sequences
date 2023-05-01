#!/usr/bin/env python3
def print_fibonacci(length):
  

  if length == 0:
    a = []
  elif length == 1:
    a = [0]
  else:
    a = [0,1]
    for n in range(length-2):
        number = a[-1]
        number2 = a[-2]
        a.append(number + number2)
    
  print(a)
