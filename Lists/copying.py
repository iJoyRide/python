myList = ["apple", "orange", "banana"]
print(myList)
print("--------------------------------")

listCopy = myList

listCopy.append("lemon")
print(listCopy)
print("--------------------------------")

print(myList)
print("--------------------------------")


listCopy2 = myList.copy()
listCopy2.append("grape")

print(listCopy2)
print("--------------------------------")
print(myList)