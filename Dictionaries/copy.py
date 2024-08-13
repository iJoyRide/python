myDict = {"name": "Max", "age": "30", "city": "New York", "state": "NY"}
print(myDict)
print("--------------------------------")

myDictCopy = myDict
myDictCopy2 = myDict.copy()

myDictCopy["email"] = "sumfeis3@gmail.com"

myDictCopy2["age"] = 400

print(myDictCopy)
print("--------------------------------")

print(myDictCopy2)
print("--------------------------------")

print(myDict)