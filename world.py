import enemies
import items
import random

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

class EnemyTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
    raise NotImplementedError()
 
def modify_player(self, player):
    raise NotImplementedError()

class StartingTile(MapTile):
	def intro_text(self):
		return """
You are standing in the rear line of a trench.
To your right is a closed door that leads into a dimly light room.
To your left is a muddy passageway.

In front of you there is an officer.
"Private Ethan, you are to report to Lt Fraser at once. Take a left and then head up and to the front lines, then take another left."

		"""
	def modify_player(self, player):
	    pass

class GenericTrench1(MapTile):
	def intro_text(self):
		return """
You are in the rear line of a muddy trench. It is eerily quiet.

		"""
	def modify_player(self, player):
	    pass

class GenericTrench2(MapTile):
	def intro_text(self):
		return """
You are standing in front of the parapet. A few hundred meters ahead of you is the German trench.
Around you are nervous men waiting for the order to attack.
		
		"""
	def modify_player(self, player):
	    pass

class GenericTrench3(MapTile):
	def intro_text(self):
		return """
You are standing in front of the parapet.
To your left stands Lt Fraser.

		"""
	def modify_player(self, player):
	    pass

class Passage1(MapTile):
	def intro_text(self):
		return """
You are standing in front of the passage leading to the front line.

		"""
	def modify_player(self, player):
	    pass

class Passage2(MapTile):
	def intro_text(self):
		return """
You are standing in the end of the passage. Ahead of you is the front line.
The only sound you can hear is the distant artillery fire from another part of the front.

		"""
	def modify_player(self, player):
	    pass

class Jump_Position(MapTile):
	def intro_text(self):
		return """
You are standnig at position to jump off and charge towards the German trench.
The deafening boom of shells hitting 300 meters in front of you almost drown out the sound of the officers whistle signaling the attack.

		"""
	def modify_player(self, player):
	    pass

class Officer_Tile(MapTile):
	def intro_text(self):
		return """
Lt Fraser stands in front of you. He looks oddly pleased with the situation.

"Private! We are jumping off any second now. Your position is just to the left here. Hopefully we'll drive the hun back!"

		"""
	def modify_player(self, player):
	    pass

class NoMansLand1(MapTile):
	def intro_text(self):
		return """
As you leap out of the trench the smattering of machine gun firing and the screams of other soldiers being hit make up a terrifying soundscape punctuated by shells hitting the German trench.
You are now running across the muddy terrain. Equal parts frightened and excited by the action.

		"""
	def modify_player(self, player):
	    pass

class NoMansLand2(MapTile):
	def intro_text(self):
		return """
Directly to your right you see a crashed airplane with British markings. You can only hope that the pilot either made it back to friendly lines or died on impact in order to evade capture.
You are now only about a hundred meters away from the German trench.

		"""
	def modify_player(self, player):
	    pass

class ArtilleryTile(MapTile):
	def intro_text(self):
		return """
You can now see the German trench, it's just 50 meters away from you.
Suddenly you hear a great roar and all you see is a blinding flash.

You were hit by an artillery shell blowing off your lower body. However another soldier carries you back to your own trench where you succumb to your injuries hours later.
		"""
	def modify_player(self, player):
		player.hp -= 100

class EnemyTile2(EnemyTile):
	def __init__(self, x, y):
		self.enemy = enemies.Landser1()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive() and self.enemy != None:
			return"""
You see a German soldier about 150 meters away. He seems to be scouting your trench.

			"""
		else:
			return"""
You are in the frontline of the trench. There lies a spent casing on the ground where you shot the scout.

			""".format(self.enemy.name)

	def modify_player(self, player):
		r = random.random()
		if r > 0.8:
			player.hp -= 15
			print("You have {} HP left.".format(player.hp))
			

class EnemyTile1(EnemyTile):
	def __init__(self, x, y):
		self.enemy = enemies.Landser2()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive() and self.enemy != None:
			return"""
a German soldier in a gas mask stands in front of you wielding a trench club.

			"""
		else:
			return"""
On the ground lies the body of the dead soldier.

			""".format(self.enemy.name)

	def modify_player(self, player):
		r = random.random()
		if r < 0.5:
			player.hp -= 35
			print("You have {} hp left.".format(player.hp))

class EnemyTile3(EnemyTile):
	def __init__(self, x, y):
		self.enemy = enemies.Stosstruppe()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive() and self.enemy != None:
			return"""
A German soldier stands in front of with you a camouflaged helmet, a bandolier and several grenades in his belt. He has an almost frenzied look in his eyes.

			"""
		else:
			return"""
Here lies the dead body of the German soldier.

			""".format(self.enemy.name)

	def modify_player(self, player):
		r = random.random()
		if r < 0.4:
			player.hp -= 40
			print("You have {} HP left.".format(player.hp))

def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None

#StartingTile = ST
#GenericTrench1 = T1
#GenericTrench2 = T2
#GenericTrench3 = T3
#Passage1 = P1
#Passage2 = P2
#Jump_Position = JP
#Officer_Tile = OT
#NoMansLand1 = N1
#NoMansLand2 = N2
#ArtilleryTile = AT
#InstaDeath = ID
#EnemyTile1 = E1
#EnemyTile2 = E2
#EnemyTile3 = E3

world_dsl = """
|  |AT|  |  |  |  |
|ID|E3|  |  |  |  |
|E1|N2|  |  |  |  |
|N1|  |  |  |  |  |
|JP|OT|T3|P2|E2|T2|
|  |  |  |P1|  |  |
|  |  |T1|T2|T1|ST|
"""

def is_dsl_valid(dsl):
	lines = dsl.splitlines()
	lines = [l for l in lines if l]
	pipe_counts = [line.count("|") for line in lines]
	for count in pipe_counts:
		if count != pipe_counts[0]:
			return False
	return True

tile_type_dict = {
	"ST": StartingTile,
	"T1": GenericTrench1,
	"T2": GenericTrench2,
	"T3": GenericTrench3,
	"P1": Passage1,
	"P2": Passage2,
	"JP": Jump_Position,
	"OT": Officer_Tile,
	"N1": NoMansLand1,
	"N2": NoMansLand2,
	"AT": ArtilleryTile,
	"E1": EnemyTile1,
	"E2": EnemyTile2,
	"E3": EnemyTile3,
	"  ": None}

world_map = []

start_tile_location = None

def parse_world_dsl():
	if not is_dsl_valid(world_dsl):
		raise SyntaxError("Shit's broke yo. Look at the DSL.")

	dsl_lines = world_dsl.splitlines()
	dsl_lines = [x for x in dsl_lines if x]

	for y, dsl_row in enumerate(dsl_lines):
		row = []
		dsl_cells = dsl_row.split("|")
		dsl_cells = [c for c in dsl_cells if c]
		for x, dsl_cell in enumerate(dsl_cells):
			tile_type = tile_type_dict[dsl_cell]
			if tile_type == StartingTile:
				global start_tile_location
				start_tile_location = x, y
			row.append(tile_type(x,y) if tile_type else None)

		world_map.append(row)