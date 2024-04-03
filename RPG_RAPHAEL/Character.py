from random import randint

class Character:
    def __init__(self, Name:str, hp:int, strength:int, dexterity:int, constitution:int, wisdom:int, intelligence:int, charisma:int)->None:
        self.name = Name
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
    
    def create_random_weight(self):
        
        self.hp = randint(0,21)
        self.strength = randint(0,21)
        self.dexterity = randint(0,21)
        self.constitution = randint(0,21)
        self.wisdom = randint(0,21)
        self.intelligence = randint(0,21)
        self.charisma = randint(0,21)
        
        
    
    def __str__(self):
        return f"|-----SEUS STATUS-----\n|Hp: {self.hp}\n|Força: {self.strength}\n|dexterity: {self.dexterity}\n|Constituição: {self.constitution}\n|wisdom: {self.wisdom}\n|intelligence: {self.intelligence}\n|charisma:{self.charisma}"

