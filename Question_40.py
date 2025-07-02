try:
  a = float("Python")
except ValueError: # Tenta converter a string "Python" num numero flutante, mas é retornado com um ValueError
  print("Not a Number")
except:
  print("This is something different")

# >> Not a number 
