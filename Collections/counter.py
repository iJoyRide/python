from collections import Counter

a = "aaaaaaaaaaaaaaaaabbbbbbbbbccccc"

my_counter = Counter(a)

print(my_counter)
print('-----------------------------')

print(my_counter.items())
print('-----------------------------')

print(my_counter.keys())
print('-----------------------------')

print(my_counter.values())
print('-----------------------------')

print(my_counter.most_common(1))
print('-----------------------------')

print(my_counter.most_common(2)[1][0])
print('-----------------------------')

print(my_counter.most_common(1)[0][1])
print('-----------------------------')