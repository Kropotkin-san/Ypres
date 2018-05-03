class Enemy:
	def __init__(self,hp,name,desc):
		self.hp = hp
		self.name = name
		self.desc = desc

	def is_alive(self):
		return self.hp > 0

class Landser1(Enemy):
	def __init__(self):
		super().__init__(name="German Soldier",
			hp=100,
			desc="Far away German landser"
			)

class Stosstruppe(Enemy):
	def __init__(self):
		super().__init__(name="German Trench Raider",
			hp=100,
			desc="Close quarters raider"
			)

class Landser2(Enemy):
	def __init__(self):
		super().__init__(name="German Soldier",
			hp=100,
			desc="No mans land Landser"
			)