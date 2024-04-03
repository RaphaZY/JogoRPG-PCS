from Barbaro.Barbaro import Barbaro
from Dragonborn.Dragonborn import Dragonborn
from Dwarf.Dwarf import Dwarf
from Elf.Elf import Elf
from Gnome.Gnome import Gnome
from Human.Human import Human
from Tiefling.Tiefling import Tiefling
from Barbaro.Barbaro_Stouf import Barbaro_Stouf
from Barbaro.Barbaro_Lightfoot import Barbaro_Lightfoot

while True:
    print("|---------------------------------------")
    print('|---------Bem Vindo Jogador-------------')
    op = input('|Digite 0 para encerrar o programa\n|Digite 1 para gerar um personagem automatico\n|Digite 2 para criar manualmente um personagem\n|Faça sua escolha: ')
    
    try:
        if op == '1':
            nome = str(input("|Digite seu nome: "))
            print("|------Escolhas sua Classe-----")
            print("|0 -> Barbaro\n|1 -> Dragonborn\n|2 -> Dwarf\n|3 -> Elf\n|4 -> Gnome\n|5 -> Human\n|6 -> Tiefling")
            type_classe = int(input("|Faça sua escolha: "))
            classe = ["Barbaro", "Dragonborn", "Dwarf", "Elf", "Gnome", "Human", "Tiefling"]
            match type_classe:
                case 0 :
                    print("|Você gostaria de evoluir seu personagem?\n|0 -> Para Cancelar\n|1-> Barbaro Pés Leves\n|2 -> Barbaro Robusto")
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
                    personagem = Dwarf(nome,0,0,0,0,0,0,0,classe[type_classe])
                    
                case 3: 
                    personagem = Elf(nome,0,0,0,0,0,0,0,classe[type_classe])
                    
                case 4: 
                    personagem = Gnome(nome,0,0,0,0,0,0,0,classe[type_classe])
                    
                case 5: 
                    personagem = Human(nome,0,0,0,0,0,0,0,classe[type_classe])
                    
                case 6: 
                    personagem = Tiefling(nome,0,0,0,0,0,0,0,classe[type_classe])
                
                case _:
                    print("|Erro: Número invalido")
                
            personagem.create_random_weight()    
            print(personagem)

        elif op == '2':
            nome = str(input("|Digite seu nome: "))
            print("|------Escolhas sua Classe-----")
            print("|0 -> Barbaro\n|1 -> Dragonborn\n|2 -> Dwarf\n|3 -> Elf\n|4 -> Gnome\n|5 -> Human\n|6 -> Tiefling")
            type_classe = int(input("|Faça sua escolha: "))
            classe = ["Barbaro", "Dragonborn", "Dwarf", "Elf", "Gnome", "Human", "Tiefling"]
            hp = int(input("|Digite seu hp: "))
            strength = int(input("|Digite sua força: "))       
            dexterity = int(input("|Digite sua dexterity: "))
            constitution = int(input("|Digite sua constituição: "))
            wisdom = int(input("|Digite sua wisdom: "))
            intelligence = int(input("|Digite sua intelligence: "))
            charisma = int(input("|Digite seu charisma: "))
            match type_classe:
                case 0 :
                    personagem = Barbaro(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 1: 
                    personagem = Dragonborn(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 2: 
                    personagem = Dwarf(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 3: 
                    personagem = Elf(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 4: 
                    personagem = Gnome(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 5: 
                    personagem = Human(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
                    
                case 6: 
                    personagem = Tiefling(nome,hp,strength,dexterity,constitution,wisdom,intelligence,charisma,classe[type_classe])
            print(personagem)

        elif op == '0':
             break

        else: 
            print("|Erro")
            break
    except:
            print("|Erro: Entrada inválida! Você deve digitar um número inteiro.")  