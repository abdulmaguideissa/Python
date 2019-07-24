# Store information with a key entry
# Key: Value
dictionary = {"a": 10, "b": 15, "c": 20, "d": 25}

# Iterating throw dictionary
# String keying
for key, value in dictionary.items():
    print 'key:', key, "\n", 'value:', value, "\n"

# Numbering keying
dict = {0: 100, 1: 150, 2: 200, 3: 250, 4: 300}
for key, value in dict.items():
    print 'key:', key, "\n", 'value:', value, "\n"

# Printing it using functions
def PrintDictionary(diction):
    for Key, Value in diction.items():
        print 'key:', Key, "\n", 'value', Value, "\n"

print("**** Using Functions *****")
PrintDictionary(dict)
