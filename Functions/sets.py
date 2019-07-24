# Python data type that stores a set of things
a = set()                         # create a new set
for num in range(1, 11):          # iterate throw this set to add some numbers
    a.add(num)

for num in a:                     # iterate throw this set to print its values
    print(num)

# To remove number duplicates from a list, use a set()
listing = [1, 1, 2, 5, 2]
new_set = set()
for n in listing:
    new_set.add(n)
print(new_set)

new_list = list()
for x in new_set:
    new_list.append(x)
print(new_list)
