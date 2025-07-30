def cars_disp(new, clist = []):
  clist.append(new)
  return clist

top_cars = cars_disp('Pagani', ['Ferrari', 'Aston', 'Lamborghini']
                     )
print(cars_disp('McLaren', top_cars))

# >> ['Ferrari', 'Aston', 'Lamborghini', 'McLaren']
