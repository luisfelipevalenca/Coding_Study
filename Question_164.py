principal = float(input('Enter the principal amount: '))
rate = float(input('Enter the rate of interest: '))
time = float(input('Enter the time in years: '))
amount = principal * (1 + rate / 100) ** time
print('The final amount after {} years is: {:.2f}'.format(time, amount))

# >> Enter the principal amount: 50
# >> Enter the rate of interest: 10
# >> Enter the time in years: 2
# >> The final amount after 2.0 years is: 60.50
