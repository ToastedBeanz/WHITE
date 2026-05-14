class Player:
    def __init__(self, inventory, name, hp, maxhp, mp, maxmp, atk, defense, act, chapt):
        self.inventory = inventory
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.mp = maxmp
        self.maxmp = maxmp
        self.atk = atk
        self.defense = defense

        # story
        self.act = act
        self.chapt = chapt
    
    def addInventory(self, item):
        self.inventory.append(item)
    
    def removeInventory(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print(f"ERROR; could not find item \"{item}\" in inventory.")
    

    def addHp(self, amnt, addmax="False"): # one function for adding normal hp and max hp :)
        if addmax:
            self.maxhp += amnt
            self.hp += amnt
        else:
            self.hp += amnt
            if self.hp > self.maxhp:
                self.hp = self.maxhp

    
    def addMp(self, amnt, addmax="False"):
        if addmax:
            self.maxmp += amnt
            self.mp += amnt
        else:
            self.mp += amnt
            if self.mp > self.maxmp:
                self.mp = self.maxmp
    
    def changeStory(self, act=None, chapter=None):
        if act is not None:
            self.act = act
        if chapter is not None:
            self.chapt = chapter



