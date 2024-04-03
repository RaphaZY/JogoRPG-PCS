from Character import Character

class Dragonborn(Character):
    def __init__(self, Name:str, hp:int, strength:int, dexterity:int, constitution:int, wisdom:int, intelligence:int, charisma:int, classe:str) -> None:
        super().__init__(Name, hp, strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.name = Name
        self.classe = classe
        self.hp = hp
        self.strength = strength + 2
        self.dexterity = dexterity 
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma + 1
    
    def __str__(self):
        return f"|------SUA CLASSE-----\n|{self.classe}\n|-----SEUS STATUS-----\n|Hp: {self.hp}\n|Força: {self.strength}\n|dexterity: {self.dexterity}\n|Constituição: {self.constitution}\n|wisdom: {self.wisdom}\n|intelligence: {self.intelligence}\n|charisma:{self.charisma}"
    
