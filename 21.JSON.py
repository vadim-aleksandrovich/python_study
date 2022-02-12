import json
filename = 'files/user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
player_1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'Awards': ['GR', 'NY', 'NV']
}

player_2 = {
    'PlayerName': 'Hilary Clinton',
    'Score': 346,
    'Awards': ['WI', 'IX', 'MI']
}

myPlayers = []
myPlayers.append(player_1)
myPlayers.append(player_2)

json.dump(myPlayers, myfile)
myfile.close()

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print('Player name is: ' + str(user['PlayerName']))
    print('Player score is: ' + str(user['Score']))
    award_count = 1
    for award in user['Awards']:
        print('Player award № ' + str(award_count) + ' is : ' + award)
        award_count += 1
myfile.close()