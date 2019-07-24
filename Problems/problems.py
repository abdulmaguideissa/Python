# Takes two bool values
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

# Returns string n times
def string_times(string, n):
    return string * n

# Returns ture if the first element or the last element of a
# list is equal to 6
def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

# Duplicate characters of a given string
def duplicate(string):
    str_result = ''
    for ch in string:
        str_result += ch * 2
    return  str_result

print(duplicate("he5o"))

# Counting even numbers
def even_counter(numbers):
    counter = 0
    for num in numbers:
        if num % 2 == 0:
            counter += 1
    return counter

nums = [1, 2, 25, 102, 36, 21, 98, 101]
print(even_counter(nums))