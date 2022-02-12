enemy = {
    'posX': 145,
    'posY': 223,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}

print(enemy.keys())
print(enemy.values())

print('Color is: ' + enemy['color'])
print('Health is ' + str(enemy['health']))
print('The object is: ' + enemy['name'] + '\n' +
      'Health: ' + str(enemy['health']) + '\n' +
      'Color: ' + enemy['color'])

enemy['rank'] = 'Admiral'  # Add new key and value
print(enemy['rank'])
del enemy['rank']          # Delete key and value
enemy['posX'] += 40        # Change value
enemy['health'] -= 30

if enemy['health'] < 80:
    enemy['color'] = 'Yellow'
elif enemy['health'] < 30:
    enemy['color'] = 'Red'



