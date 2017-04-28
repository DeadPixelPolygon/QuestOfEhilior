class enemy:
    def __init__ (self, name, desc, hp, ap, acc, spd):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.ap = ap
        self.acc = acc
        self.spd = spd
         
goblin = enemy('Goblin', 'A green, foul creature', 7, 5, 5, 1) #grasslands and goblin hideout
wolf = enemy('Wolf', 'A fast predator.', 13, 9, 7, 8) #hills
kraken = enemy('Kraken', 'A monster from the deepest waters',25 , 20, 5, 9) #sea
crab = enemy('Giant Crab', 'It digs itself in the sand and jumps out of it to attack people.', 15, 9, 7, 3) #coast
ghost = enemy('Ghost', 'It is the undead spirit of an ill-fated adventurer.', 35, 15, 7, 7) #haunted hills
spider = enemy('Giant Spider', 'This creature has poison fangs and eight long feet. Just nope!', 10, 8, 8, 9) #forest
mutant = enemy('Mutant', 'Mutants are Goblins who are infected with the virus of the swamp', 40, 17, 6, 8) #swamp
