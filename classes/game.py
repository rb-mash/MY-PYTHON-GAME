import random
from.magic import Spell
from.inventory import Item

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class person:
    def __init__(self, hp, mp, atk, df, magic, items):

        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.items = items
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp>self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost


    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Choose an action: " + bcolors.ENDC)
        for items in self.actions:
            print("    ",str(i) + ": " + items)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Choose a spell: " + bcolors.ENDC)       
        for spell in self.magic:
            print("    ",str(i) + ": " , spell.name, "(cost: " + str(spell.cost) + ")")
            i += 1
    
    def choose_items(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Choose an item: " + bcolors.ENDC)
        for item in self.items:
            print("    ",str(i) + ": " + bcolors.OKGREEN + item.name + bcolors.ENDC , "(" + bcolors.WARNING + "Description:", bcolors.ENDC + item.description+")")
            i += 1


class enemy:
    def __init__(self, hp, mp, atk, df, magic):
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
