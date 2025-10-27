import random 

class karaktar: 
    def __init__(self, namn, halsa, attackkraft):
        self.namn = namn 
        self.halsa = halsa
        self.max_halsa = halsa
        self.attackkraft = attackkraft
        self.cooldown = 0

        