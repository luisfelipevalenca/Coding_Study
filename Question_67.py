a = 200
b = 200

if(a==b):
  # pass >> OK
  # print(a/(a-b)) >> ZeroDivisionError: division by zero
   print(a/a-b) # OK
else:
  print('a and be are equal')

# >> -199.0
