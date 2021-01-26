class Character:
    def __init__(self,name,lvl):
        self.name = name
        self.lvl = lvl
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
        
        self.change_hp()
        self.change_en()
               
        print("Todos os atributos já começando com o mesmo valor do seu level! (Até o level 15!)") 
        # All atributes start with the same value as your level! (Until level 15!)

    def __str__ (self):
        output = ('\n'+self.name+', Level '+str(self.lvl))
        output += ('\nHP: '+str(self.hp)+' | EN: '+str(self.en))
        output += ('\nFOR - '+str(self.str))
        output += ('\nACU - '+str(self.acu))
        output += ('\nPRE - '+str(self.pre))
        output += ('\nDEX - '+str(self.dex))
        output += ('\nVIT - '+str(self.vit))

        return output

    def combat_bonus(self,name,number):
        pass         
    
    def check_atr_min(self,number):
        if self.lvl < 15:
            if number < self.lvl:
                print("\nObedeça a regra de atributos mínimos!")
                # Obey the minimun attribute rule
                return False
            else:
                return True
        else:
            if number < 15:
                print("\nObedeça a regra de atributos mínimos!")
                # Obey the minimun attribute rule
                return False
            else:
                return True            
    
    def change_hp(self,bonus=0):
        self.hp = bonus + (self.vit + self.lvl)*10
        if self.hp < 20:
            self.hp = 20
            
    def change_en(self,haki=0,cyber_lvl=0):        
        self.en = (self.str + self.acu + self.pre + self.dex + self.vit) + (self.lvl * 10)    

    def change_lvl(self,number):
        self.lvl = number     

    def change_str(self,number):
        if self.check_atr_min(number):
            self.str = number 
            self.change_en()
            
    def change_acu(self,number):
        if self.check_atr_min(number):
            self.acu = number 
            self.change_en()
            
    def change_pre(self,number):
        if self.check_atr_min(number):
            self.pre = number 
            self.change_en()
            
    def change_dex(self,number):
        if self.check_atr_min(number):
            self.dex = number 
            self.change_en()
            
    def change_vit(self,number):
        if self.check_atr_min(number):
            self.vit = number 
            self.change_hp()
            self.change_en()
        
    
        
        
Tyr = Character('Tyr', 10)   
print(Tyr)
Tyr.change_vit(15)
print(Tyr)
