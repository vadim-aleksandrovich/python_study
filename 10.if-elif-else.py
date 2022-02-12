x = 26
if x == 25:
    print('Right')
else:
    print('Wrong')

age = 5
if age <= 4:
    print('You are baby!')
elif age < 12:
    print('You are kid')
elif (age >= 12) and (age < 19):  # example and. enough condition: "age < 19"
    print('You are teenager')
else:
    print('You are adult!')


cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
german_cars = ['bmw', 'vw']
if 'vw' in cars:
    print('VW is in the list')
else:
    print("We don't have vw right now")

for car in cars:
    if car in german_cars:
        print(car + ' is German car')
    else:
        print(car + ' is not German car')