import random

class Hero:
    # We want our hero to have a default "starting health",
    # so we can set that in the function header.

    #This is the constructor/initializer
    def __init__(self, name, starting_health = 100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''

        # We know the name of our hero, so we assign it here
        self.name = name
        # Similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # When a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def battle(self, *args):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''

        # todo: Fight each hero until a victor emerges
        # Phases to implement:
        # 1) Randomly choose winner, print the name of the victor
        # Hint: Look into random library, more specifically the choice method

        hero_names = []
        hero_names.append(self.name)

        for hero in args:
            hero_names.append(hero.name)
        

        winner = random.choice(hero_names)
        losers = []

        for name in hero_names:
            if name != winner:
                losers.append(name)
        print(f'{winner} has defeated {losers}')

        return winner


    