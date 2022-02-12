
# https://docs.python.org/2.4/lib/standard-encodings.html           - Encoding list
import time

inputFile = 'files/passwords.txt'
outputFile = 'files/my_passwords.txt'

myInputfile = open(inputFile, mode='r', encoding='latin-1')
myOutputfile = open(outputFile, mode='a', encoding='latin-1')   # r - read only, w - rewrite , a - append to file

searching_string = "vadik"
# print(myInputFile.read())                      # Read all file

#for line in myInputFile:
#   print('Hello ' + line.strip())          # Read file and start string with 'Hello'

count = 0
myOutputfile.write('\n\nStart searching password: ' + searching_string +'\n')

for num, line in enumerate(myInputfile, 1):

    if searching_string in line:
        print('Line № ' + str(num) + ':\t ' + line.strip())
        myOutputfile.write('Founded password: ' + line)
        count += 1

print('Total number of passwords with string - ' + searching_string + ' is: ' + str(count))
myOutputfile.write('Total number of passwords with string - ' + searching_string + ' is: ' + str(count))

myInputfile.close()
myOutputfile.close()