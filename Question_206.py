def fibonacci (n):
    sequence = []

    a,b = 0,1

    while len(sequence) < n:
      sequence.append(a)
      a,b=b, a+b
    return sequence

terms = 10
fib_sequence = fibonacci(terms)
print(f'Fibonacci Sequence up to {terms} terms: {fib_sequence}')

# >> Fibonacci Sequence up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
