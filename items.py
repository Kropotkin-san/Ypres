class Item():
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return "{} {}".format(self.name, self.description)

class Weapon(Item):
	def __init__(self, damage, description, name, ammunition, magazine_loaded, capacity):
		self.damage = damage
		self.magazine_loaded = magazine_loaded
		self.capacity = capacity
		self.ammunition = ammunition
		super().__init__(name, description)

	
	def __str__(self):
		return "{} {}".format(self.name, self.description,)

class Grenade(Item):
	def __init__(self, damage, description, name, ammunition):
		self.damage = damage
		self.ammunition = ammunition
		super().__init__(name, description)

	
	def __str__(self):
		return "{} {} Amount:{}".format(self.name, self.description, self.ammunition)

	
class Enfield(Weapon):
	def __init__(self):
		super().__init__(name = "Lee-Enfield Rifle",
			description = "Bolt action rifle chambered in .303 british. Standard issue.",
			damage = 85,
			magazine_loaded = 10,
			capacity = 10,
			ammunition = 150)

class Webley(Weapon):
	def __init__(self):
		super().__init__(name = "Webley Revolver",
			description = "Standard issue Webley revolver chambered in .455 Webley. Stolen from a dead officer.",
			damage = 30,
			magazine_loaded = 6,
			capacity = 6,
			ammunition = 37)

class Grenade(Grenade):
	def __init__(self):
		super().__init__(name = "Mills bomb",
			description = "Standard issue british handgrenade.",
			damage = 100,
			ammunition = 5)