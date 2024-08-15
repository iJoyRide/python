from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

print(d)
print('-----------------------------')

d.pop()
print(d)
print('-----------------------------')

d.extendleft([4,5,6])
print(d)
print('-----------------------------')

d.rotate(-2)
print(d)
print('-----------------------------')


