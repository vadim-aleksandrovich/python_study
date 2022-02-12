def create_record(name, telephone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record('Nick', '+234565', 'Minsk')
user2 = create_record('Mike', '+234565', 'Moscow')

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give Medals to personts"""
    for person in persons:
        print('Congratulation, ' + person.title() + ' your medal is ' + medal)


give_award('For Victory', 'Nick', 'Mike')
give_award('For Brave', 'Lex', 'Fix', 'Pix')



