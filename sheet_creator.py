class Character:
    def __init__(self,name,lvl):
        self.name = name
        self.lvl = lvl
        self.haki = 0
        self.perception = 0
        self.stealth = 0
        self.professions = []
        self.professions_lvl = []

        if (lvl>15):
            self.str = 15
            self.acu = 15
            self.pre = 15
            self.dex = 15
            self.vit = 15 
        else:          
            self.str = lvl
            self.acu = lvl
            self.pre = lvl
            self.dex = lvl
            self.vit = lvl
            
        self.dmg_melee = self.str
        self.dmg_ranged = self.acu
        self.na_melee = self.pre
        self.na_ranged = self.pre
        self.nd_bloq = self.dex
        self.nd_dodge = self.dex
        self.res = self.vit/2
        self.change_hp()
        self.change_en()       

        self.percep_stealth_teste_config(self) 
               
        print("Todos os atributos já começando com o mesmo valor do seu level! (Até o level 15!)") 
        # All atributes start with the same value as your level! (Until level 15!)

    def convert_profession_level (self, level):
        text = ['Amador (Novato)','Amador (Intermediário)',
        'Amador (Veterano)','Profissional (Novato)',
        'Profissional (Intermediário)','Profissional (Veterano)',
        'Especialista (Novato)','Especialista (Intermediário)',
        'Especialista (Veterano)','Mestre (Novato)',
        'Mestre (Intermediário)','Mestre (Veterano)','Grão Mestre']
        return (text[level-1])

    def __str__ (self):
        output = ('\n'+self.name+', Level '+str(self.lvl))
        output += ('\nHP: '+str(self.hp)+' | EN: '+str(self.en))
        output += ('\nFOR - '+str(self.str))
        output += ('\nACU - '+str(self.acu))
        output += ('\nPRE - '+str(self.pre))
        output += ('\nDEX - '+str(self.dex))
        output += ('\nVIT - '+str(self.vit))
        output += ('\n')
        output += ('\nDANO (Melee) -- '+str(self.dmg_melee))
        output += ('\nDANO (Ranged) - '+str(self.dmg_ranged))
        output += ('\nNA (Melee) ---- '+str(self.na_melee))
        output += ('\nNA (Ranged) --- '+str(self.na_ranged))
        output += ('\nND (Bloqueio) - '+str(self.nd_bloq))
        output += ('\nND (Esquiva) -- '+str(self.nd_dodge))
        output += ('\nRES ----------- '+str(self.res))
        output += ('\nPERCEPÇÃO ----- '+str(self.perception))
        output += ('\nFURTIVIDADE --- '+str(self.stealth))
        output += ('\n\n')
        for i,prof in enumerate(self.professions):
            output += (str(i) + '. ' +str(prof) + ' - ' + str(self.convert_profession_level(self.professions_lvl[i])) + '\n')      
        return output       

    def change_perception(self,number):
        self.perception = number
        
    def change_stealth(self,number):
        self.stealth = number

    def add_profession (self, profession, level):
        self.professions.append(profession)
        self.professions_lvl.append(level)
    
    def change_hp(self,bonus=0):
        self.hp = bonus + (self.vit + self.lvl)*10
        if self.hp < 20:
            self.hp = 20
            
    def change_en(self,bonus=0):        
        self.en = (self.str + self.acu + self.pre + self.dex + self.vit) + (self.lvl * 10) + (self.haki * 15) + bonus

    def change_lvl(self,number):
        self.lvl = number     
        self.change_hp()
        self.change_en()  

    def change_haki(self,number):
        self.haki = number     
        self.change_en() 

    def change_atrib(self,atrib,number):
        # STR = 0 / ACU = 1 / PRE = 2 / DEX = 3 / VIT = 4 #
        if (atrib==0):
            old_bonus = (self.dmg_melee-self.str)
            self.str = number 
            self.change_subatrib(0,old_bonus)

        elif (atrib==1):
            old_bonus = (self.dmg_ranged-self.acu)
            self.acu = number 
            self.change_subatrib(1,old_bonus)

        elif (atrib==2):
            old_bonus = (self.na_melee-self.pre)
            old_bonus2 = (self.na_ranged-self.pre)
            self.pre = number 
            self.change_subatrib(2,old_bonus)
            self.change_subatrib(3,old_bonus2)

        elif (atrib==3):
            old_bonus = (self.nd_bloq-self.dex)
            old_bonus2 = (self.nd_dodge-self.dex)
            self.dex = number 
            self.change_subatrib(3,old_bonus)
            self.change_subatrib(4,old_bonus2)

        elif (atrib==4):
            old_bonus = (self.res-self.vit/2)
            self.vit = number 
            self.change_subatrib(5,old_bonus)
            self.change_hp()
        self.change_en()    

    def change_subatrib(self,subatrib,bonus=0):
        # dmg_melee = 0 / dmg_ranged = 1 / na_melee = 2 / na_ranged = 3 / nd_bloq = 4 / nd_dodge = 5 / res = 6#
        if (subatrib==0):
            self.dmg_melee = self.str + bonus
        elif (subatrib==1):
            self.dmg_ranged = self.acu + bonus
        elif (subatrib==2):
            self.na_melee = self.pre + bonus
        elif (subatrib==3):
            self.na_ranged = self.pre + bonus
        elif (subatrib==4):
            self.nd_bloq = self.dex + bonus
        elif (subatrib==5):
            self.nd_dodge = self.dex + bonus
        elif (subatrib==6):
            self.res = int(round((self.vit/2) + bonus,0))

    def percep_stealth_teste_config(self,change=0,new_values=[]):
        """if change = 1, obey the order: \n
        [unit_percep,
        unit_stealth,
        unit_prof]"""
        if (change == 1):
            self.unit_percep = new_values[0]
            self.unit_stealth = new_values[1]
            self.unit_prof = new_values[2]
        else:
            self.max_profession_lvl = 13
            self.max_perception = 36 # Vantagens -> Não foram consideradas arma única, haki nem Arqueólogo;
            self.max_stealth = 30 # Vantagens -> Não foram consideradas arma única, haki nem Ladrão;
            self.success_chances = [90,75,50,25,10] # Chances de sucesso dos testes em percentagem (Muito Fácil, Fácil, Médio, Difícil, Muito Difícil)      
            self.difficulty_name = ['Muito Fácil','Fácil','Médio','Difícil','Muito Difícil']     
            # Condição: Quando o valor de percepção do player for igual a max_perception, testes médios deverão se tornar testes Muito Fáceis.
            self.unit_percep = (self.success_chances[0]-self.success_chances[2])/self.max_perception # Quanto cada unidade de percepção aumenta a chance de sucesso
            self.unit_stealth = (self.success_chances[0]-self.success_chances[2])/self.max_stealth # Quanto cada unidade de percepção aumenta a chance de sucesso
            self.unit_prof = 65/(self.max_profession_lvl-1) # Quanto cada level da percepção aumenta a chance de sucesso


    def percep_stealth_test(self,type,difficulty,bonus=0):
        """type = (1=Perception / 2=Stealth)
        test_difficulty: \n
        [0] - Very Easy \n
        [1] - Easy \n
        [2] - Normal \n
        [3] - Difficult \n
        [4] - Very Difficult"""    
        #if (difficulty>4)or(difficulty<0):
        #    print('Dificuldade entre 0 e 4:\n [0] - Very Easy \n [1] - Easy \n [2] - Normal \n [3] - Difficult \n [4] - Very Difficult')
        #    return ()
        #if (type>2)or(type<0):
        #    print('Tipos: \n 1 - Percepção  \n 2 - Furtividade')
        #    return()

        if (type==1):
            player_value = self.perception + bonus
            unit_perc = self.unit_percep
            text = ("PERCEPÇÃO")
        elif (type==2):
            player_value = self.stealth + bonus
            unit_perc = self.unit_stealth
            text = ("FURTIVIDADE")

        success_chance = self.success_chances[difficulty] + (player_value * unit_perc)
        success_chance = 5 * round(success_chance/5)
        if (success_chance >= 100):
            success_chance = 100
        print('\n=== TESTE DE '+str(text)+' ===\n')
        dice_min = int(20 - (20 * success_chance/100) + 1)
        line1 = ('DIFICULDADE: ' + self.difficulty_name[difficulty])
        line2 = ('CHANCE DE SUCESSO: ' + str(success_chance) + '%')
        line3 = ('SUCESSO IGUAL OU MAIS: ' + str(dice_min))
        print(line1 + '\n' + line2 + '\n' + line3)

    def profession_test(self,profession_number,difficulty,bonus=0):
        success_chance = self.success_chances[difficulty] + (self.professions_lvl[profession_number] * self.unit_prof)
        if (self.professions_lvl[profession_number]==13):
            success_chance += self.unit_prof
        success_chance = 5 * round(success_chance/5)
        if (success_chance >= 100):
            success_chance = 100
        print('\n=== TESTE DE ' + str(self.professions[profession_number]) + ' ===\n')
        dice_min = int(20 - (20 * success_chance/100) + 1)
        line1 = ('DIFICULDADE: ' + self.difficulty_name[difficulty])
        line2 = ('CHANCE DE SUCESSO: ' + str(success_chance) + '%')
        line3 = ('SUCESSO IGUAL OU MAIS: ' + str(dice_min))
        print(line1 + '\n' + line2 + '\n' + line3)


Tyr = Character('Tyr', 11)   
atributos = [23,11,22,20,37] # STR = 0 / ACU = 1 / PRE = 2 / DEX = 3 / VIT = 4 #
subatributos = [18,10,18,3,26,5,11] # dmg_melee = 0 / dmg_ranged = 1 / na_melee = 2 / na_ranged = 3 / nd_bloq = 4 / nd_dodge = 5 / res = 6#

for i,value in enumerate(atributos):
    Tyr.change_atrib(i,value)
for i,value in enumerate(subatributos):
    Tyr.change_subatrib(i,value)

Tyr.change_hp(50)
Tyr.change_en(20)
Tyr.change_haki(3)
Tyr.change_perception(16)
Tyr.add_profession('NAVEGADOR',6)
Tyr.add_profession('COZINHEIRO',7)
print(Tyr)

Tyr.percep_stealth_test(2,4)
Tyr.profession_test(0,4)
