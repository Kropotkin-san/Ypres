from player import Player
import world
from collections import OrderedDict

def play():
	world.parse_world_dsl()
	player = Player()
	while player.is_alive():
		try:
			room = world.tile_at(player.x, player.y)
			print(room.intro_text())
			room.modify_player(player)
			choose_action(room, player)
		
		except KeyboardInterrupt:
			print("")
			exit()
		except EOFError:
			print("")
			exit()

def get_available_actions(room, player):
	actions = OrderedDict()
	print("Available orders are:")
	if player:
		action_adder(actions, 'q', player.exit, "Quit the game")
	if player.inventory:
		action_adder(actions, 'i', player.print_inventory, "Print Inventory")
	if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
		action_adder(actions, '1', player.enfieldattack, "Shoot with your rifle")
		action_adder(actions, '2', player.webleyattack, "Shoot with your revolver")
		action_adder(actions, 'g', player.grenadeattack, "Throw a grenade")
	#if player.webleycheck != 0:
	#	action_adder(actions, 'reload revolver', player.webley_reload)
	#if player.enfieldcheck != 0:
	#	action_adder(actions, 'reload rifle', player.enfield_reload)
	else:
		if world.tile_at(room.x, room.y - 1):
			action_adder(actions, 'n', player.move_North, "Go North")
		if world.tile_at(room.x, room.y + 1):
			action_adder(actions, 's', player.move_South, "Go South")
		if world.tile_at(room.x + 1, room.y):
			action_adder(actions, 'e', player.move_East, "Go East")
		if world.tile_at(room.x - 1, room.y):
			action_adder(actions, 'w', player.move_West, "Go West")
	return actions

def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

def choose_action(room, player):
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input("Actions: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("Invalid Action!")
play()