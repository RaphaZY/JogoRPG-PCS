from random import randint

class Character:
    def __init__(self, Name:str, hp:int, strength:int, dexterity:int, constitution:int, wisdom:int, intelligence:int, charisma:int)->None:
        self.name = Name
        self._hp = hp
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._wisdom = wisdom
        self._intelligence = intelligence
        self._charisma = charisma
        self._type_strenght = {
            'Incorpóreo':[0],
            'Incapaz':[1,2,3,4,5],
            'Fraco':[6,7,8,9],
            'Mediano':[10,11],
            'Forte':[12,13,14,15],
            'Super Poderoso':[16,17,18,19,20],
            'Imbatível':[21]
        }
        self._type_decterity = {
            'Desacordado':[0],
            'Abatido':[1,2,3,4,5],
            'Desajeitado':[6,7,8,9],
            'Regular':[10,11],
            'Ágil':[12,13,14,15],
            'Ninja':[16,17,18,19,20],
            'Imperceptível':[21]
        }
        self._type_constitution = {
            'Espectro':[0],
            'Enfermo':[1,2,3,4,5],
            'Frágil':[6,7,8,9],
            'Saudável':[10,11],
            'Durão':[12,13,14,15],
            'Super Resistente':[16,17,18,19,20],
            'Imortal':[21]
        }
        self._type_wisdom = {
            'Inconsciente':[0],
            'Irracional':[1,2,3,4,5],
            'Desatento':[6,7,8,9],
            'Simples':[10,11],
            'Perspicaz':[12,13,14,15],
            'Filósfo':[16,17,18,19,20],
            'Iluminado':[21]
        }
        self._type_intelligence = {
            'Inanimado':[0],
            'Incivilizado':[1,2,3,4,5],
            'Parvo':[6,7,8,9],
            'Medíocre':[10,11],
            'Estudado':[12,13,14,15],
            'Gênio':[16,17,18,19,20],
            'Onisciente':[21]
        }
        self._type_charisma = {
            'Aberração':[0],
            'Inexpressivo':[1,2,3,4,5],
            'Rude':[6,7,8,9],
            'Sociável':[10,11],
            'Persuasivo':[12,13,14,15],
            'Influente':[16,17,18,19,20],
            'Ídolo':[21]
        }
    
    def create_random_character(self):
        
        self._hp = 5 + randint(0,21)
        self._strength = randint(0,21)
        self._dexterity = randint(0,21)
        self._constitution = randint(0,21)
        self._wisdom = randint(0,21)
        self._intelligence = randint(0,21)
        self._charisma = randint(0,21)

    def _calc_Descrition_Atribute(self, value, descrition)-> None:
        for x in descrition:
            for y in descrition[x]:
                if value == y:
                    return x
    
    def typeStrenght(self):
        return self._calc_Descrition_Atribute(self._strength, self._type_strenght)

    def typeDexterity(self):
        return self._calc_Descrition_Atribute(self._dexterity, self._type_decterity)

    def typeConstitution(self):
        return self._calc_Descrition_Atribute(self._constitution, self._type_constitution)

    def typeWisdom(self):
        return self._calc_Descrition_Atribute(self._wisdom, self._type_wisdom)
    
    def typeIntelligence(self):
        return self._calc_Descrition_Atribute(self._intelligence, self._type_intelligence)
    
    def typeCharisma(self):
        return self._calc_Descrition_Atribute(self._charisma, self._type_charisma)
        
        
    
    def __str__(self):
        return f"|---------------------------------\n|-----------SEUS STATUS----------\n|Hp: {self._hp}\n|Força: {self._strength} ----------> {self.typeStrenght()}\n|Destreza: {self._dexterity} -------> {self.typeDexterity()}\n|Constituição: {self._constitution} ---> {self.typeConstitution()}\n|Sabedoria: {self._wisdom} ------> {self.typeWisdom()}\n|Inteligencia: {self._intelligence} ---> {self.typeIntelligence()}\n|Carisma: {self._charisma} --------> {self.typeCharisma()}"


