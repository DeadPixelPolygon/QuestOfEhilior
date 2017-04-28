class weapon:
    def __init__ (self, name, desc, ap, acc):
        self.name = name
        self.desc = desc
        self.ap = ap
        self.acc = acc
        
s_dagger = weapon('short dagger', 'A very weak basic weapon.', 5, 8) 
GoldenSword = weapon('golden sword', 'A shiny golden sword.', 10, 9)
KingsBlade = weapon('Kingsblade', 'It was once used by the greatest king in Ehilior.', 25, 8)
