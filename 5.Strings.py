myString = 'Hello World'
name = 'mr vaDim aleKSanDroVich'

print(name.title())
print(name.upper())
print(name.lower())

print('First string\nSecond string\n\nThird string with space')     # \n — new line
print('Messages:\n\t1.Message1\n\t* Message2\n\t- Message3')        # \t — tab
print('Your name is: ' + name.lower())


a = ". @@ ....  * * ...  https://www.aleksandrovich.it@.   .   @@"

print('---------------------------------------------')
print(a)
print('---------------------------------------------')
print(a.rstrip())       # Delete spaces from left side
print(a.lstrip())       # Delete spaces form right side
print(a.strip())        # Delete all spaces

print(a.strip('@'))
print(a.strip('. @ *'))
# Python code to illustrate the working of strip()
string = '@@@@Geeks for Geeks@@@@@'

# Strip all '@' from beginning and ending
print(string.strip('@'))

string = 'www.Geeksforgeeks.org'

# '.grow' removes 'www' and 'org' and '.'
print(string.strip('.grow'))
