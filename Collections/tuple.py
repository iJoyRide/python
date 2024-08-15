from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)

print(pt)
print('-----------------------------')

print(f"the coordinates are {pt.x} and {pt.y}")
print('-----------------------------')
