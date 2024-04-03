from Character import Character

class Barbaro(Character):
    def __init__(self, name:str, hp:int, strength:int, dexterity:int, constitution:int, wisdom:int, intelligence:int, charisma:int, classe:str) -> None:
        super().__init__(name, hp, strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.name = name
        self.classe = classe
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity + 2
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
    
    def __str__(self):
        return f"|------SUA CLASSE-----\n|{self.classe}\n|-----SEUS STATUS-----\n|Hp: {self.hp}\n|Força: {self.strength}\n|dexterity: {self.dexterity}\n|Constituição: {self.constitution}\n|wisdom: {self.wisdom}\n|intelligence: {self.intelligence}\n|charisma:{self.charisma}"
    
