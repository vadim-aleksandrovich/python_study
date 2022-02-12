from modules.heroClass import *

myHero = Hero('Riki', 4, 'Assassin')
mySuperHero = SuperHero('Sniper', 15, 'Human', 25)


myHero.show_hero()
mySuperHero.show_hero()
mySuperHero.makemagic(30)
mySuperHero.magiclevel = 50     # dont work, bcs we use "__magic" to block access out of class
mySuperHero.show_hero()
mySuperHero.setMagic(5)
mySuperHero.show_hero()
mySuperHero.show_hero()


