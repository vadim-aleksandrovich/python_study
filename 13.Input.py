print('------------------------------------------------------------------------------')

name = input("Please enter Your name: ")
print("Hello " + name)

num1 = input('Enter X: ')
num2 = input('Enter Y: ')

print('------------------------------------------------------------------------------')

sumStr = num1 + num2            # By Default sum of string
sumInt = int(num1) + int(num2)
print(sumStr)
print(sumInt)

print('------------------------------------------------------------------------------')

message = ''
while True:
    message = input('Enter Password: ')
    if message == 'secret':
        print('login')
        break
    print(message + 'Password not correct')

print('Password was: ' + message)

print('------------------------------------------------------------------------------')

myList = []
mag = ''
while mag != 'STOP':
    mag = input('Enter new item, and STOP to finish ')
    if mag != 'STOP':
        myList.append(mag)

print(myList)