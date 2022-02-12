import sys

filename = 'files/my_passwordss.txt'
while True:    #  For working input filename by user
    try:
        print('Inside TRY')
        myfile = open(filename, mode='r', encoding='Latin-1')
    except Exception:
        print('Inside EXCEPT')
        print('Error Found')
        print(sys.exc_info()[1])        # Show error message
        filename = input('Please, Enter correct filename: ')
    else:
        print('Inside ELSE')
        print(myfile.read())
        sys.exit()                      # Stop programm from here
    finally:                            # NOT NECESSARY !! continue program. isn't depends of have you mistake or not
        print('Inside FINALLY')

print('---------------------- EOF ----------------------')