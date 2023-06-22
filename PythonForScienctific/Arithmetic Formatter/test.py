list1 = ["apple", "orange", "pineapple", "kiwi", "mango"]
list2 = ["red", "blue", "yellow", "green", "cyan"]
list3 = ["a","b","c","d","e"]
list = []
for i in range(len(list1)):
    a = max(len(item) for item in [list1[i],list2[i], list3[i]])
    list.append(a)
print(list)