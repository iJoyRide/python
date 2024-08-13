myDict = {"name": "Max", "age": "30", "city": "New York", "state": "NY"}
print(myDict)
print("--------------------------------")

try: 
    print(myDict["name"])
except:
    print("Error.")
print("--------------------------------")

try: 
    print(myDict["lastname"])
except:
    print("Error.")
print("--------------------------------")
    
for value in myDict:
    print(value)
print("--------------------------------")

    
for key in myDict.keys():
    print(value)
print("--------------------------------")

for key, value in myDict.items():
    print(key, value)