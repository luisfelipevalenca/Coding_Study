try:
  1/0
except ArithmeticError: # python verifica primeiro esse bloco, embora o subsequente também seja verdadeiro, ele para após o seguinte print
  print('It is wrong')
except ZeroDivisionError:
  print('Any number cannot be divided by zero')
except:
  print('Something else went wrong')

# >> It is wrong
