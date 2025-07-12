class Counter:
    count = 0

    def increment(self):
        Counter.count += 1

counter1 = Counter()
counter1.increment()

# print(counter1.count) # >>  1
counter2 = Counter()
counter2.increment()
# print(counter2.count) #  >> 2
print(Counter.count)

# >> 2
