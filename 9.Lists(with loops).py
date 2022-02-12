cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for car in cars:
    print(car.upper())

for x in range(0, len(cars), 1):
    print(cars[x])

number_list = list(range(0, 10))
print(number_list)

for x in number_list:
    x *= 2
    print(x)
number_list.sort(reverse=True)
print(number_list)

print(min(number_list))
print(max(number_list))
print(sum(number_list))


cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[2:3]
print(mycars)
mycars = cars[:3]
print(mycars)
mycars = cars[-2:]
print(mycars)

mycars = cars[:] # Create copy of list
endpoint = cars # Create new end poind for cars
endpoint.append('Alfa Romeo')
mycars.append('Polo')
print(mycars)
print(cars)