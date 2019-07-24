c = []
for element in range(1, 10):
    c.append(element * 2)
print(c)

# Squaring numbers from 1 to 7
squared = []
for num in range(1, 7):
    squared.append(num ** 2)
print(squared)

empty = []
for num in range(6, 0, -1):
    empty.append(num ** 2)
print 'Using append', empty

# Using list comprehension
em = [x ** 2 for x in range(6, 0, -1)]
print 'Using comprehension', em
