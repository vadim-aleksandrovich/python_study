import random

enemy = {
    'posX': 145,
    'posY': 223,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())    # For creating isolated, independed elements

for ene in all_enemies:
    enemy['posX'] = random.randint(0, 100)
    enemy['posY'] = random.randint(0, 100)

    print(ene)

all_enemies[5]['health'] = 30
all_enemies[2]['posY'] += 10
print('------------------------------------------------------------------------------')
for ene in all_enemies:
    print(ene)




