#Imports the libraries that hold the needed resources.
import items
import world
import random

#Defines the player class
class Player:
	def __init__(self):
		#Creates the player inventory and it's items
		self.inventory = [items.Enfield(),
						items.Webley(),
						items.Grenade()]
		#Player hp				
		self.hp = 100
		#Player starting position
		self.x = world.start_tile_location[0]
		self.y = world.start_tile_location[1]

		#Creates local variables needed for the reload and attack action
		#Amount of loose ammo
		self.enfield_ammo = items.Enfield().ammunition
		#Amount loaded in magazine
		self.enfield_loaded = items.Enfield().magazine_loaded
		#Magazine capacity
		self.enfield_capacity = items.Enfield().capacity

		self.webley_ammo = items.Webley().ammunition
		self.webley_loaded = items.Webley().magazine_loaded
		self.webley_capacity = items.Webley().capacity

		self.grenade_ammo = items.Grenade().ammunition

	#Defines the print_inventory action
	def print_inventory(self):
		print("""
			Inventory:""")
		#For loop that prints out all items in the player inventory
		for item in self.inventory:
			print('* ' + str(item))

	def check_ammo(self):
		print("")
		print("Webley Ammunition: {} Loaded: {}".format(self.webley_ammo, self.webley_loaded))
		print("Enfield Ammunition: {} Loaded: {}".format(self.enfield_ammo, self.enfield_loaded))

	#Function that is used in the game loop in order to check if player can reload the rifle
	def enfieldcheck(self):	
		self.enfieldcheckvar = self.enfield_capacity - self.enfield_loaded
		if self.enfieldcheckvar != 0:
			enfieldcheck = True
		else:
			enfieldcheck = False
		return self.enfieldcheckvar
		return enfieldcheck

	def webleycheck(self):	
		self.webleycheckvar = self.webley_capacity - self.webley_loaded
		if self.webleycheckvar != 0:
			webleycheck = True
		else:
			webleycheck = False
		return self.webleycheckvar
		return webleycheck

	def webley_reload(self):
		self.webley_loaded += self.webleycheckvar
		self.webley_ammo -= self.webleycheckvar

	def enfield_reload(self):
		self.enfield_loaded += self.enfieldcheckvar
		self.enfield_ammo -= self.enfieldcheckvar


	def enfieldattack(self):
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		r1 = random.random()
		r2 = random.random()
		if self.enfield_loaded > 0:
			print("")
			print("You fire your enfield at the enemy.")
			self.enfield_loaded -= 1
			if r1 < 0.2:
				print("You miss.")
			elif r1 < 0.8:
				enemy.hp -= items.Enfield().damage
				if not enemy.is_alive():
					print("The soldier sinks to the ground. Mortally wounded.")
				else:
					if r2 > 0.5:
						print("You hit the soldier in the arm.")
					else:
						print("You hit the soldier in the lower torso.")
			else:
				enemy.hp -= 100
				print("The soldier sinks to the ground. Mortally wounded")

		else:
			print("You need to reload!")

	def webleyattack(self):
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		r1 = random.random()
		r2 = random.random()
		if self.webley_loaded > 0:
			print("")
			print("You fire your webley at the enemy.")
			self.webley_loaded -= 1
			if r1 < 0.35:
				print("You miss.")
			elif r1 > 0.35:
				enemy.hp -= items.Webley().damage
				if not enemy.is_alive():
					print("The soldier sinks to the ground. Mortally wounded.")
				else:
					print("You wound the soldier.")
		else:
			print("You need to reload!")

	def grenadeattack(self):
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		r1 = random.random()
		r2 = random.random()
		self.grenade_ammo -= 1
		if r1 < 0.5:
			print("The grenade misses the soldier.")
		else:
			enemy.hp -= items.Grenade().damage
			if r2 < 0.4:
				print("The soldier collapses as his left leg is blown clean off.")
			elif r2 < 0.8:
					print("The soldier drops to the ground desperately holding onto his abdomen while screaming.")
			else:
				print("The soldier collapses to the ground clutching what used to be his arm.")


	#Checks if player is actually alive
	def is_alive(self):
		return self.hp > 0
	#Exit function
	def exit(self):
		print("Exiting.")
		exit()
		
	#Movement function
	def move(self, dx ,dy):
		self.x += dx
		self.y += dy

	def move_North(self):
		self.move(dx = 0, dy = -1)

	def move_South(self):
		self.move(dx = 0, dy = 1)

	def move_East(self):
		self.move(dx = 1, dy = 0)

	def move_West(self):
		self.move(dx = -1, dy = 0)