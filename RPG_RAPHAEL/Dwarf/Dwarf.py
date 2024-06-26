from Character import Character

class Dwarf(Character):
    def __init__(self, name:str, hp:int, strength:int, dexterity:int, constitution:int, wisdom:int, intelligence:int, charisma:int, classe:str) -> None:
        super().__init__(name, hp, strength, dexterity, constitution, wisdom, intelligence, charisma)
        self._name = name
        self._classe = classe
        self._hp = hp
        self._strength = strength
        self._dexterity = dexterity 
        self._constitution = constitution + 2
        self._wisdom = wisdom
        self._intelligence = intelligence
        self._charisma = charisma
    
   
