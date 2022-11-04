list1 = ["a","b","c","d","d","e"]

try:
    print(list1[13])
except IndexError:
    print("Indices Error! The indices out of list")