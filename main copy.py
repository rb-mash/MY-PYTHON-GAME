from classes.game import bcolors, person

magic =[{"name": "Fire", "cost": 10, "dmg": 70},
        {"name": "Thunder", "cost": 15, "dmg": 80},
        {"name": "Dark Wind", "cost": 20, "dmg": 100},
        {"name": "Sasuke", "cost": 30, "dmg": 7000},]

    
player = person(480, 60, 90, 100, magic)
enemy = person(1200, 65, 45, 80, magic)


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)


while running:
	print("===============================")
	player.choose_action()
	choice = input("Choose Action: ")
	index = int(choice) - 1

	if index == 0:
		dmg = player.generate_damage()
		enemy.take_damage(dmg)
		print("You attacked for", dmg, "damage!", "Enemy HP", enemy.get_hp())
	elif index == 1:
		player.choose_magic()
		magic_choice = input("Choose Magic: ")
		index = int(magic_choice) - 1
		print("You chose", player.get_spell_name(index), "for", player.get_spell_mp_cost(index))
		mdmg = player.generate_spell_damage(index)
		enemy.take_damage(mdmg)
		print("You attacked for", mdmg, "spell damage!", "Enemy HP", enemy.get_hp())

	else:
		running = False


