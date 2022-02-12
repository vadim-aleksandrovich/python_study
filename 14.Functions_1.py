def print_hello(name):
    """Print Hello"""
    print('Congratulations, ' + name + ' wish you all the best!')


def sum_elements(x, y):
    return x + y


def get_factorial(x):
    """Calcualte factorial of number x"""
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print('------------------------------------------------------------------------------')

print_hello('Vadim')
print_hello('Snezhik')

print('------------------------------------------------------------------------------')

sum_elements(10, 20)

print('------------------------------------------------------------------------------')

x = sum_elements(23, 22)
print(x)

print('------------------------------------------------------------------------------')
y = 3
get = get_factorial(y)
print("!" + str(y) + ' = ' + str(get))

print('------------------------------------------------------------------------------')

for i in range(1, 12):
    print(str(i) + '!\t = ' + str(get_factorial(i)))