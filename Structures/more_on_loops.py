# Practice more on loops
# using the indexing method of for loop instead of element

a = ["apple", "banana", "strawperry"]
for index in range(len(a)):
    for inner in range(index + 1):
        print(a[index])

# Combining functions and loops to produce a number factorial
def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        return num
    else:
        while num > 1:
            fact = fact * num
            num = num - 1
        return fact

result = factorial(6)
print(result)

# Finding A fibonacci series till a given number
# with the aid of dynamic programming, create a lookup table for the first two numbers
def fibonacci(num):
    F = [0] * num        # Initializes a list of size num to zeros
    F[0] = 0
    F[1] = 1
    for i in range(2, num):
        F[i] += F[i - 1] + F[i - 2]
        print(F[i])
    return F[num - 1]
fibo = fibonacci(8)
print(fibo)
