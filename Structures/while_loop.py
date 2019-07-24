# Studying the syntax of the while loop
total = 0
num = 1
while num < 5:
    total += num
    num += 1
print(total)

user_list = [5, 4, 2, -8, -6, 5, 5, 1]
totalnum = 0
index = 0
while (index < len(user_list)) and (user_list[index] > 0):
    totalnum += user_list[index]
    index += 1
print(totalnum)
