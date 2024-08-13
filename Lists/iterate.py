myList = ["apple", "orange", "banana"]

for fruit in myList:
    print(fruit)
print("--------------------------------")

for i in range(len(myList)):
    print(f"{i}:{myList[i]}")
print("--------------------------------")
    
if "pineapple" in myList:
    print(True)
else:
    print(False)