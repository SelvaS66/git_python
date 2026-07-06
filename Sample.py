#year = input('Enter your year of birth: ')
##age = 2026 - int(year)
#print('You are ' + str(age) + ' years old.')

msg = 'welcome to python programming'
print(msg)
print(msg[0])
print(msg[0:7])
print(msg[11:18])
print(msg[11:])
print(msg[:6])
print(msg[:-1])
print(msg[1:-1])

print(len(msg))

print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.strip())
print(msg.replace('python', 'java'))
print(msg.split())
print(msg.split('o'))
print(msg.find('python'))
print('python' in msg)


#Arithmetic Operators
x = 10
y = 3
s= x/y
print(s)
s= x//y
print(s)
s= x%y
print(s)
s= x**y
print(s)
print(x>y)


a=10.34
print(round(a))
print(abs(-a))