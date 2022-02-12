class Hero():
    """ Class to create Hero for our Game """
    def __init__(self, name, level, race):  # obligatory method
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """ Print all parameters of this hero """
        description = (
                self.name + "\n- Level is: " +
                str(self.level) + "\n- Race is " +
                self.race + "\n- Health is " +
                str(self.health)).title()
        print(description)

    def level_up(self):
        """Upgrade level of Hero"""
        self.level += 1
        print('Hero ' + self.name + ' get level ' + str(self.level))

    def move(self):
        """Move our hero"""
        print('Hero ' + self.name + ' Has already started moving')

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """ Class to create Super Hero from Hero """
    def __init__(self, name, level, race, magiclevel):
        """ Initiate our Super Hero """
        super().__init__(name, level, race)     # copy parameters and methods from Hero class
        self.magiclevel = magiclevel
        self.__magic = 100                      # __ - block access to change value out of class

    def makemagic(self, power):
        self.__magic -= power
        print('Hero ' + self.name + ' making magic with power ' + str(power))

    def setMagic(self, power):
        self.__magic = power
        print('Magic of ' + self.name + ' has been changed to ' + str(self.__magic))

    def show_hero(self):
        """ Print all parameters of this hero """
        description = (
                self.name + "\n- Level is: " +
                str(self.level) + "\n- Race is " +
                self.race + "\n- Health is " +
                str(self.health)) + "\n- Magic is " + \
                str(self.__magic).title()
        print(description)