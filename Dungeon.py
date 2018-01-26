print("Welcome to the Dungeon of Djibouti, where the explorers await their feat and the monsters wait to eat!  Are you ready for the search of Dayo's treasure?")
#The Character layout
class Character(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = {
            'wooden.sword': 1,
            'gold.sword': 0,
            'titanium.sword': 0,
            'uranium.sword': 0
            }
#The different weapons you will be able to use against the monsters
    def attack(self,Monster):
        print(f"attacking {Monster.name}")
        if self.inventory['wooden.sword'] > 0:
            dmg = 2
        elif self.inventory['gold.sword'] > 0:
                dmg = 6
        elif self.inventory['titanium.sword'] > 0:
                dmg = 12
        elif self.inventory['uranium.sword'] > 0:
                dmg = 25
        Monster.hp -= dmg
#Layout for the monsters
class Monster(object):
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
#Monster names and individual attriubutes
Monster1 = Monster('Poisoned Toad',20, 1)
Monster2 = Monster('Cranky Caboose', 25, 3)
Monster3 = Monster('Quick Rat', 35, 6)
Monster4 = Monster('Jabba the Mutt', 45, 8)
Monster5 = Monster('Barbarous Bunny', 60, 12)
Monster6 = Monster('Hellish Horse', 80, 14)
Monster7 = Monster('Demonic Dragon',150, 20)
#Character name
Troy = Character('Troy')

#Battle against the first Monster.  Type in attack to attack the monster.
print ("It's Level 1.  You have encountered a Poisoned Toad")
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster1.hp > 0:
        Troy.attack(Monster1)
        print(f"{Monster1.name} is now at {Monster1.hp} health.")
if Monster1.hp <= 0:
    print ("You defeated the Poisoned Toad.")

print(f"The {Monster1.name} dropped nothing.  Maybe the next monster will....")

print(f"Level 2 is here, and you encounter the {Monster2.name}.")
#Battle against the second monster
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster2.hp > 0:
        Troy.attack(Monster2)
        print(f"{Monster2.name} is now at {Monster2.hp} health.")
if Monster3.hp <= 0:
    print ("You defeated the Cranky Caboose.")

print(f"The {Monster2.name} dropped a gold sword. Congratulations!  Good stuff, you have made it to Level 3. Your next opponent is the {Monster3.name}")
#You have obtained and are now using the gold sword.
Troy.inventory = {
            'wooden.sword': 0,
            'gold.sword': 1,
            'titanium.sword': 0,
            'uranium.sword': 0
            }
#Battle against the third monster
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster3.hp > 0:
        Troy.attack(Monster3)
        print(f"{Monster3.name} is now at {Monster3.hp} health.")
if Monster3.hp <= 0:
    print ("You defeated the Quick Rat.")

print("That's impressive.  You defeated that speedy rat.  Onto Level 4.")
#Battle against the fourth monster
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster4.hp > 0:
        Troy.attack(Monster4)
        print(f"{Monster4.name} is now at {Monster4.hp} health.")
if Monster4.hp <= 0:
    print ("You defeated Jabba the Mutt.")

print(f"Good work, you are now more than half way from obtaining Dayo's treasure.  Level 5 begins now.")
#Battle against the fifth monster
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster5.hp > 0:
        Troy.attack(Monster5)
        print(f"{Monster5.name} is now at {Monster5.hp} health.")
if Monster5.hp <= 0:
    print ("You defeated the Barbarous Bunny.")

print(f"You're really good. The Barbarous Bunny dropped a Titanium Sword. Congratulations!  Level 6 will begin shortly.")
#You have obtained and are now using the titanium sword
Troy.inventory = {
            'wooden.sword': 0,
            'gold.sword': 0,
            'titanium.sword': 1,
            'uranium.sword': 0
            }
#Battle against the sixth monster
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster6.hp > 0:
        Troy.attack(Monster6)
        print(f"{Monster6.name} is now at {Monster6.hp} health.")
if Monster6.hp <= 0:
    print ("You defeated the Hellish Horse.")

print(f"You slayed the Hellish Horse, and now you made it to the boss battle.  This one is no easy task.  Here, let me help you...")

print("Congratulations, you have obtained the uranium sword!  You will need all the help you can get for this battle!")
#You have obtained and are now using the uranium sword
Troy.inventory = {
            'wooden.sword': 0,
            'gold.sword': 0,
            'titanium.sword': 0,
            'uranium.sword': 1
            }
#Final Boss Battle
choice = input("What do you want to do? ")
if choice == 'attack':
    while Monster7.hp > 0:
        Troy.attack(Monster7)
        print(f"{Monster7.name} is now at {Monster7.hp} health.")
if Monster7.hp <= 0:
    print ("You defeated the Demonic Dragon.")
#You won the treasure you were searching for!
print("Congrats!  You defeated the final boss!  Dayo's treasure is now all yours!  You can finally live that luxurious life you always wanted.")

print("Thanks for playing!")