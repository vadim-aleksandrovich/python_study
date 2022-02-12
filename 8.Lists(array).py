cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']
print(len(cities))
print(cities[0])
print(cities[-1])
print(cities[2].title())
cities[2] = 'Tula'
print(cities[2])
cities.append('Kursk')

cities.append('Yalta')
cities.insert(2, 'Feodosiya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula') # remove first found elemnt


deleted_city = cities.pop() # Defauld delete last one item and get it
print("Deleted city is: " + deleted_city)
print(cities)

print(cities.sort())
print(cities)

cities.reverse()
print(cities)