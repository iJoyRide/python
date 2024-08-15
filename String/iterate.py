greeting = "Hello, World Today"
news = "My Name is"
sub_string = greeting[::2]

print(sub_string)
print('-----------------------------')

if 'ell' in greeting:
    print('yes')
print('-----------------------------')
    
print(greeting.find('o'))
print('-----------------------------')

print(greeting.startswith('Hello'))
print('-----------------------------')

print(greeting.endswith('World'))
print('-----------------------------')

print(greeting.replace('World', 'Universe'))
print('-----------------------------')

split_string = greeting.split()
print(split_string)
print('-----------------------------')

split_string = greeting.split(',')
print(split_string)
print('-----------------------------')

print(greeting + " " + news)