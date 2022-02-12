from modules.heroClass import Hero

# ---------------------------- MAIN ----------------------------
hero1 = Hero('Riki', 5, 'Assasin')
hero2 = Hero('Ogre Mag', 4, 'Orc')

hero1.show_hero()
hero2.move()
hero1.level_up()
hero1.show_hero()
hero2.set_health(50)

hero2.show_hero()