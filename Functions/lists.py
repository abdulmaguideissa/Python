# Lists in python is something like arrays in c/c++

a = [55, 88, 8878, -5, 97, 102, 5]
print(a)
a.append(5)
a.append("what is it?")
print(a)
a.pop()
print(a[5])

# Swapping elements of a list
b = ["banana", "apple", "microsoft"]
tmp = b[0]
b[0] = b[2]
b[2] = tmp
print(b)
