from Barbaro.Barbaro import Barbaro
from Dragonborn.Dragonborn import Dragonborn
from Dwarf.Dwarf import Dwarf
from Dwarf.Dwarf_Hill import Dwarf_Hill
from Dwarf.Dwarf_Mountain import Dwarf_Mountain
from Elf.Elf import Elf
from Elf.Elf_Dark import Elf_Dark
from Elf.Elf_High import Elf_High
from Elf.Elf_Wood import Elf_Wood
from Gnome.Gnome import Gnome
from Gnome.Gnome_Forest import Gnome_Forest
from Gnome.Gnome_Rock import Gnome_Rock
from Human.Human import Human
from Tiefling.Tiefling import Tiefling
from Barbaro.Barbaro_Stouf import Barbaro_Stouf
from Barbaro.Barbaro_Lightfoot import Barbaro_Lightfoot

class Controlar():
    def controlar(self):
        while True:

            print("|\n|\n|---------------------------------------")
            print("|-------------RPG do Senai--------------")
            print("|---------------------------------------")
            print('|---------Bem Vindo Jogador-------------')
            op = input('|Digite 0 para encerrar o programa\
                    \n|Digite 1 para gerar um personagem automatico\
                    \n|Digite 2 para criar manualmente um personagem\
                    \n|Faça sua escolha: ')
            
            try:

                if op == '1':
                    nome = str(input("|Digite seu nome: "))
                    print("|---------------------------------------")
                    print("|----------Escolha sua Classe------------")
                    print("|0 -> Barbaro\
                        \n|1 -> Draconato\
                        \n|2 -> Anão\
                        \n|3 -> Elfo\
                        \n|4 -> Gnomo\
                        \n|5 -> Humano\
                        \n|6 -> Ladrão")

                    type_classe = int(input("|Faça sua escolha: "))
                    classe = ["Barbaro", "Draconato", "Anão", "Elfo", "Gnomo", "Humano", "Ladrão"]
                    
                    match type_classe:
                        case 0 :
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1 -> Barbaro Pés Leves\
                                \n|2 -> Barbaro Robusto")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Barbaro", "Barbaro Pés Leves","Barbaro Robusto"]
                            match type_classe:
                                case 0 :
                                    personagem = Barbaro(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Barbaro_Lightfoot(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Barbaro_Stouf(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case _:
                                    print("|Erro: Número invalido")   

                        case 1: 
                            personagem = Dragonborn(nome,0,0,0,0,0,0,0,classe[type_classe])
                            
                        case 2: 
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Anão da Colina\
                                \n|2 -> Anão da Montanha")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Anão", "Anão da Colina","Anão da Montanha"]
                            match type_classe:
                                case 0 :
                                    personagem = Dwarf(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Dwarf_Hill(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Dwarf_Mountain(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case _:
                                    print("|Erro: Número invalido") 

                        case 3: 
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Elfo Grande\
                                \n|2 -> Elfo da Floresta\
                                \n|3 -> Elfo Negro")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Elfo", "Elf Grande","Elfo da Floresta", "Elfo Negro"]
                            match type_classe:
                                case 0 :
                                    personagem = Elf(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Elf_High(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Elf_Wood(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 3 :
                                    personagem = Elf_Dark(nome,0,0,0,0,0,0,0,classe[type_classe])  
                                case _:
                                    print("|Erro: Número invalido") 
                            
                        case 4: 
                            print("\n|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Gnomo da Floresta\
                                \n|2 -> Gnomo da Pedra")
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Gnomo", "Gnomo da Floresta","Gnomo da Pedra"]
                            match type_classe:
                                case 0 :
                                    personagem = Gnome(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Gnome_Forest(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Gnome_Rock(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case _:
                                    print("|Erro: Número invalido") 
                                    
                        case 5: 
                            personagem = Human(nome,0,0,0,0,0,0,0,classe[type_classe])
                            
                        case 6: 
                            personagem = Tiefling(nome,0,0,0,0,0,0,0,classe[type_classe])
                        
                        case _:
                            print("|Erro: Número invalido")
                        
                    personagem.create_random_character()   
                    print("|\n|--------------------------------")
                    print(f"|--------{classe[type_classe]}---------")
                    print(personagem)
                    enter = input("|\n|\n|-------Enter para seguir--------")
                    

                elif op == '2':
                    nome = str(input("|Digite seu nome: "))
                    print("|-------------------------------------")
                    print("|----------Escolha sua Classe----------")
                    print("|0 -> Barbaro\
                        \n|1 -> Draconato\
                        \n|2 -> Anão\
                        \n|3 -> Elfo\
                        \n|4 -> Gnomo\
                        \n|5 -> Humano\
                        \n|6 -> Ladrão")
                    
                    type_classe = int(input("|Faça sua escolha: "))
                    
                    if type_classe > 6 or type_classe < 0:
                        print("Erro: Valor maior que 6 ou menor que 0")
                        break
                    else:
                        pass 
                    
                    classe = ["Barbaro", "Draconato", "Anão", "Elfo", "Gnomo", "Humano", "Ladrão"]
                    hp = 5 + int(input("|Digite seu hp: "))         
                    strength = int(input("|Digite sua Força: "))       
                    
                    if strength > 21 or strength < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 
                    
                    dexterity = int(input("|Digite sua Destreza: "))
                    
                    if dexterity > 21 or dexterity < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 

                    constitution = int(input("|Digite sua Constituição: "))

                    if constitution > 21 or constitution < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 

                    wisdom = int(input("|Digite sua Sabedoria: "))

                    if wisdom > 21 or wisdom < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 

                    intelligence = int(input("|Digite sua Inteligencia: "))

                    if intelligence > 21 or intelligence < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 

                    charisma = int(input("|Digite sua Carisma: "))

                    if charisma > 21 or charisma < 0:
                        print("Erro: Valor maior que 21 ou menor que 0")
                        break
                    else:
                        pass 

                    match type_classe:
                        case 0 :
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1 -> Barbaro Pés Leves\
                                \n|2 -> Barbaro Robusto")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Barbaro", "Barbaro Pés Leves","Barbaro Robusto"]

                            match type_classe:
                                case 0 :
                                    personagem = Barbaro(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Barbaro_Lightfoot(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 : 
                                    personagem = Barbaro_Stouf(nome,0,0,0,0,0,0,0,classe[type_classe])  
                                case _:
                                    print("|Erro: Número invalido") 

                        case 1: 
                            personagem = Dragonborn(nome,0,0,0,0,0,0,0,classe[type_classe])
                            
                        case 2: 
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Anão da Colina\
                                \n|2 -> Anão da Montanha")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Anão", "Anão da Colina","Anão da Montanha"]
                            
                            match type_classe:
                                case 0 :
                                    personagem = Dwarf(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Dwarf_Hill(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Dwarf_Mountain(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case _:
                                    print("|Erro: Número invalido") 

                        case 3: 
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Elfo Grande\
                                \n|2 -> Elfo da Floresta\
                                \n|3 -> Elfo Negro")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Elfo", "Elf Grande","Elfo da Floresta", "Elfo Negro"]
                            
                            match type_classe:
                                case 0 :
                                    personagem = Elf(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Elf_High(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Elf_Wood(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 3 :
                                    personagem = Elf_Dark(nome,0,0,0,0,0,0,0,classe[type_classe])  
                                case _:
                                    print("|Erro: Número invalido") 
                            
                        case 4: 
                            print("|---------------------------------------")
                            print("|Você gostaria de evoluir seu personagem?\
                                \n|0 -> Para Cancelar\
                                \n|1-> Gnomo da Floresta\
                                \n|2 -> Gnomo da Pedra")
                            
                            type_classe = int(input("|Faça sua escolha: "))
                            classe = ["Gnomo", "Gnomo da Floresta","Gnomo da Pedra"]
                            
                            match type_classe:
                                case 0 :
                                    personagem = Gnome(nome,0,0,0,0,0,0,0,classe[type_classe])
                                case 1 : 
                                    personagem = Gnome_Forest(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case 2 :
                                    personagem = Gnome_Rock(nome,0,0,0,0,0,0,0,classe[type_classe]) 
                                case _:
                                    print("|Erro: Número invalido") 
                                    
                        case 5: 
                            personagem = Human(nome,0,0,0,0,0,0,0,classe[type_classe])
                            
                        case 6: 
                            personagem = Tiefling(nome,0,0,0,0,0,0,0,classe[type_classe])
                        
                        case _:
                            print("|Erro: Número invalido")
                        
                    personagem.create_random_character()    
                    print(personagem)
                    enter = input("|\n|\n|-------Enter para seguir-------")

                elif op == '0':
                    break

                else: 
                    print("|Erro")
                    break

            except:
                print("|Erro: Entrada inválida! Você deve digitar um número inteiro.") 
        