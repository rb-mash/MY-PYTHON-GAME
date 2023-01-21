from classes.game import bcolors, person
from classes.magic import Spell
from classes.inventory import Item


# Dark magic
Fire = Spell("Fire", 10, 90, "Dark")
Thunder = Spell("Thunder", 15, 140, "Dark")
Dark_wind = Spell("Dark Wind", 20, 200, "Dark")
Sasuke = Spell("Sasuke", 40, 800, "Dark")
Dragon = Spell("Dragon", 60, 1200, "Dark")
Naruto = Spell("Lightning", 80, 1600, "Dark")
Quake = Spell("Quake",80, 2400, "Dark")

# Light magic
cure = Spell("Cure", 10, 100, "Light")
cura = Spell("Cura", 15, 180, "Light")
curb = Spell("Curb", 20, 240, "Light")

#Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)

# Instantiate People    
player = person(480, 60, 90, 100, [Fire, Thunder, Dark_wind, Sasuke, Dragon, Naruto, Quake, cure, cura, curb])
enemy = person(1200, 65, 45, 80, [])


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
	player_hp = player.get_hp()
	player_mp = player.get_mp()

	print("================================")
	print("Your HP:", bcolors.OKGREEN + bcolors.BOLD + str(player.get_hp()), "/", str(player.get_max_hp()) + bcolors.ENDC)
	print("Your MP:", bcolors.OKGREEN + bcolors.BOLD + str(player.get_mp()), "/", str(player.get_max_mp()) + bcolors.ENDC)
	print("================================")
	print("Enemy HP:", bcolors.FAIL + bcolors.BOLD + str(enemy.get_hp()), "/", str(enemy.get_max_hp()) + bcolors.ENDC)
	print("Enemy MP:", bcolors.FAIL + bcolors.BOLD + str(enemy.get_mp()), "/", str(enemy.get_max_mp()) + bcolors.ENDC)
	print("===============================")


	player.choose_action()
	choice = input("Choose Action: ")
	index = int(choice) - 1

	if index == 0:
		# normal attack
		dmg = player.generate_damage()
		enemy.take_damage(dmg)
		print("You attacked for", dmg, "damage!", "Enemy HP", enemy.get_hp())

	
	elif index == 1:
		 # Display magic attack options
		player.choose_magic()

		 # Player chooses magic attack
		magic_choice = input("Choose Magic: ")
		index = int(magic_choice) - 1

		current_mp = player.get_mp()
		spell = player.magic[index]
		mdmg = spell.generate_damage()
		cost = spell.cost
		

		
		print("\nYou chose", spell.name, "for", cost)#(index))
		 

		if spell.cost > current_mp:
			print(bcolors.FAIL + bcolors.BOLD + "\nYou don't have enough MP!\n" + bcolors.ENDC)
			continue

		#process the spell
		if spell.type == "Light":
			player.heal(mdmg)
			print(bcolors.OKBLUE + bcolors.BOLD + "\nYou healed for", mdmg, "damage!\n" + bcolors.ENDC)


		elif spell.type == "Dark":
			player.reduce_mp(cost)
			enemy.take_damage(mdmg)
			print("You attacked", spell.name, "for", mdmg, "spell damage!", "Enemy HP", enemy.get_hp())

	
	print("\n===============================")
	
	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	
	print("Enemy attacks for", enemy_dmg, "damage!", "\nPlayer HP", player.get_max_hp())
	print("\n===============================")

	
	if player.get_hp() <= 0: 
		running = False
		print(bcolors.FAIL + bcolors.BOLD + "GAME OVER! You lost" + bcolors.ENDC)

	elif enemy.get_hp() <= 0:
		print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
		running = False


