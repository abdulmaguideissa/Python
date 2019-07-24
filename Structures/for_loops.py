# Introduction to for loops
a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)

b = [20, 56, 97, 45]
total = 0
for element in b:
    total = total + element
    print(element)

print("Total is: ")
print(total)

# Creating a list of a set of numbers using
# list() & range()
c = list(range(1, 5))
print("List using list")
print(c)

# Printing the multiple of three
def MultipleOfThree(arr[]):
totalmul = 0
for num in range(1, 8):
    if (num % 3) == 0:
        totalmul = totalmul + num
print(totalmul)

