try:
  file = open('example.txt','r')
  content = file.read()

except FileNotFoundError:
  print('Error: File not found.')
finally:
  file.clode()
  print('File closed.')

# >> Error: File not found.
# >> NameError: name 'file' is not defined
