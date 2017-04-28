#imports
from weapons import *
from enemies import *
from items import *
import time
import random

player_items = []

class playable:
	def __init__ (self, name, weapon, maxhp, hp, ap, acc, px, py, lastmove):
		self.name = name
		self.weapon = weapon
		self.maxhp = maxhp
		self.hp = hp
		self.ap = ap
		self.acc = acc
		self.px = px
		self.py = py
		self.lastmove = lastmove

#========================================================================================================================
#all owerworld tiles
Overworld = {
	#row 1
	'land1_1':{ #tile name
		'tx': 1, #x coordinate
		'ty': 1, #y coordinate
		'barrier': True, #barrier y/n
		'type': 'waves', #tile type
		'enemy': None, #enemy on tile
		'item': None, #item on tile
		'weapon': None, #weapon on tile
		'desc': None}, #description of tile
	'land2_1':{
		'tx': 2,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land3_1':{
		'tx': 3,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land4_1':{
		'tx': 4,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land5_1':{
		'tx': 5,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land6_1':{
		'tx': 6,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land7_1':{
		'tx': 7,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land8_1':{
		'tx': 8,
		'ty': 1,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	#row 2
	'land1_2':{
		'tx': 1,
		'ty': 2,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land2_2':{
		'tx': 2,
		'ty': 2,
		'barrier': False,
		'type': 'sea',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'West and north is sea big waves. East is calmer sea and south is the coast.'},
	'land3_2':{
		'tx': 3,
		'ty': 2,
		'barrier': False,
		'type': 'sea',
		'enemy': 'kraken',
		'item': None,
		'weapon': None,
		'desc': 'North and west is more sea, but it has too big waves for a boat. In the east is calmer water. To the south is coast.'},
	'land4_2':{
		'tx': 4,
		'ty': 2,
		'barrier': False,
		'type': 'sea',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'North and south is sea. In the southwest and the east is coast.'},
	'land5_2':{
		'tx': 5,
		'ty': 2,
		'barrier': False,
		'type': 'coast',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'The north and the west is occupied by the sea. South and east is coastland. There is a castle in the southeast.'},
	'land6_2':{
		'tx': 6,
		'ty': 2,
		'barrier': False,
		'type': 'coast',
		'enemy': 'crab',
		'item': None,
		'weapon': None,
		'desc': 'In the north is the sea, but it has too big waves for boats. East and west is coast and south is a castle.'},
	'land7_2':{
		'tx': 7,
		'ty': 2,
		'barrier': False,
		'type': 'coast',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'North and east is sea with high waves. South and west is coast.'},
	'land8_2':{
		'tx': 8,
		'ty': 2,
		'barrier': True,
		'type': 'waves',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	#row 3
	'land1_3':{
		'tx': 1,
		'ty': 3,
		'barrier': True,
		'type': 'mountain',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land2_3':{
		'tx': 2,
		'ty': 3,
		'barrier': False,
		'type': 'coast',
		'enemy': 'crab',
		'item': None,
		'weapon': None,
		'desc': 'North there is sea and east is coast. To the south is grasslands and west is a mountain'},
	#row 6
	'land3_6':{
		'tx': 3,
		'ty': 6,
		'barrier': False,
		'type': 'grasslands',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'There is coast in all direction but south. in the east and north is the waves. You can already smell the salt.'},
	#row 7
	'land1_7':{
		'tx': 1,
		'tz': 7,
		'barrier': True,
		'type': 'mountain',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': None},
	'land2_7':{
		'tx': 2,
		'tz': 7,
		'barrier': False,
		'type': 'grasslands',
		'enemy': 'Goblin',
		'item': None,
		'weapon': None,
		'desc': 'North is coast and west-south grasslands. In the west is a mountain.'},
	'land3_7':{
		'tx': 3,
		'ty': 7,
		'barrier': False,
		'type': 'grasslands',
		'enemy': None,
		'item': None,
		'weapon': None,
		'desc': 'In the north and west is a coast. To the south and east are grasslands with rocks. There seems to be a house far in the east.'},
		}

#========================================================================================================================
#globals
global Playable
global gonorth
global goeast
global gosouth
global gowest

#variables	
inp = '> '
t = time
line = ('===================================================================================')
saveCounter = 0

#========================================================================================================================
#title screen
def title():
	print(' __   __   __   __   __   __   __   __ ')
	print('|  |_|  |_|  |_|  |_|  |_|  |_|  |_|  |')
	print('\                                     /')
	print(' \___________________________________/')
	print('  |                                 |')
	print('  |         QUEST OF EHILIOR        |')
	print('  |           Alpha 1.0.1           |')
	print('  |                                 |')
	print('  |                                 |')
	print('  |                                 |')
	print('  |                                 |')
	print('  |                                 |')
	print('  |                                 |')
	print('  |              _____              |')
	print('  |             /  |  \             |')
	print('  |            /   |   \            |')
	print('  |            |   |   |            |')
	print('  |            |   |   |            |')
	print('  |            |   |   |            |')
	print('  |____________|___|___|____________|')
	menu()
	
def menu():
	print ('         ====================\n          START THE GAME (s)\n          HELP           (h)\n          INFORMATION    (i)\n          QUIT           (q)\n         ====================')
	title_inp = input(inp)
	if title_inp == 's':
		print ('Easy (e) or hard (h) game?')
		difficulty_inp = input(inp)
		if difficulty_inp == 'e':
			difficulty = 'e'
		elif difficulty_inp == 'h':
			difficulty = 'h'
		else:
			invalid_inp()
			menu()
		saveLoader()
		nameCreator()
	elif title_inp == 'h':
		gamehelp()
	elif title_inp == 'q':
		print('Bye !')
		quit
	elif title_inp == 'i':
		info()
	else:
		invalid_inp()
		menu()

#save loading
def saveLoader():
		print ('Do you want to load your save? (y/n)')
		saveLoader_inp = input(inp)
		if saveLoader_inp == 'y':
			try:
				player = playable (saveList[0], saveList[1], saveList[2], saveList[3], saveList[4], saveList[5], saveList[6], saveList[7], saveList[8])
				desc()
			except NameError:
				print('No save file found! Continuing with character creation.')
				nameCreator()
		elif saveLoader_inp == 'n':
			nameCreator()
		else:
			invalid_inp()
			saveLoader()
	
#define player name
def nameCreator():
	global p_name
	global player
	print('The gods speak to you: What shall be your name, adventurer? (3 to 8 characters long)')
	name_inp=input(inp)
	if (len(name_inp))<=2 or (len(name_inp))>=9:
		print('Invalid name. 3 to 8 characters long!')
		nameCreator()
	elif (len(name_inp))>=3:
		p_name = name_inp
		#player creating
		player = playable (name_inp, s_dagger.name, 10, 10, s_dagger.ap, s_dagger.acc, 3, 7, None)
		intro()

#game initiation
def intro():
	print('\nTHE GODS HAVE CHOSEN YOU, '+player.name+', TO FIND NEW LAND FOR YOUR PEOPLE TO LIVE IN. GOOD LUCK ON YOUR QUEST!')
	ontile(False)

#========================================================================================================================
#informs the player about the tile he is standing on
def ontile(noenemy):

	#checks if tile is a barrier
	def checkbarrier():
		if (Overworld['land'+str(player.px)+'_'+str(player.py)]['barrier']) == True:
			print (line)
			if (Overworld['land'+str(player.px)+'_'+str(player.py)]['type']) == 'waves':
				print ('The waves here are too high. Even a boat would sink here.')
			else:
				print ('The '+Overworld['land'+str(player.px)+'_'+str(player.py)]['type']+'here are too cold. You can not go this way.')
			print (line)
			t.sleep(1)
			#makes the player go to the last tile he was standing on
			if player.lastmove == 'n_y':
				player.py += 1
				ontile(True)
			elif player.lastmove == 'p_x':
				player.px -= 1
				ontile(True)
			elif player.lastmove == 'p_y':
				player.py -= 1
				ontile(True)
			elif player.lastmove == 'n_x':
				player.px += 1
				ontile(True)
		else:
			desc()
	
	def desc():
		print (line)
		print ('Your location: '+Overworld['land'+str(player.px)+'_'+str(player.py)]['type']) #type of tile
		print ('\n'+Overworld['land'+str(player.px)+'_'+str(player.py)]['desc']) #description of tile
		checkenemy()
			
	def checkenemy():
		if (Overworld['land'+str(player.px)+'_'+str(player.py)]['enemy']) == None or noenemy == True:
			print ('\nEnemies: There are no enemies here.') #no enemies on tile
			checkitem()
		else:
			enemy = (Overworld['land'+str(player.px)+'_'+str(player.py)]['enemy'])
			print ('\nA '+Overworld['land'+str(player.px)+'_'+str(player.py)]['enemy']+' is here.') #enemies on tile
			if enemy == 'Goblin':
				goblin_battle()
			elif enemy == 'Wolf':
				wolf_battle()
			elif enemy == 'Kraken':
				kraken_battle()
			elif enemy == 'Giant crab':
				crab_battle()
			
	def checkitem():
		if (Overworld['land'+str(player.px)+'_'+str(player.py)]['item']) == None:
			print ('\nItems: There are no items here.') #no items on tile
			checkweapon()
		else:
			print ('\nItems: '+Overworld['land'+str(player.px)+'_'+str(player.py)]['item'].name) #items on tile
			checkweapon()

	def checkweapon():
		if (Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']) == None:
			print ('\nItems: There are no weapons here.') #no items on tile
			print (line)
			go()
		else:
			print ('\nWeapons: '+Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon'].name) #weapons on tile
			print (line)
			go()
			
	t.sleep(1)
	checkbarrier()

#moving menu
def go():
	game_inp = input(inp)
	while (game_inp != 'go north' and game_inp != 'go east' and game_inp != 'go south' and game_inp != 'go west' and game_inp != 'quit' and game_inp != 'stats' and game_inp != 'get item' and game_inp != 'get weapon' and game_inp != 'save'):
		invalid_inp()
		go()
	if game_inp == 'go north':
		gonorth()
	elif game_inp == 'go east':
		goeast()
	elif game_inp == 'go south':
		gosouth()
	elif game_inp == 'go west':
		gowest()
	elif game_inp == 'stats':
		stats()
	elif game_inp == 'get item':
		getitem()
	elif game_inp == 'get weapon':
	 	getweapon()
	elif game_inp == 'save':
		save()
	elif game_inp == 'quit':
		quit

#also moving
def gonorth():
	player.py -= 1
	player.lastmove = 'n_y'
	ontile(False)
	
def goeast():
	player.px += 1
	player.lastmove = 'p_x'
	ontile(False)
	
def gosouth():
	player.py += 1
	player.lastmove = 'p_y'
	ontile(False)
	
def gowest():
	player.px -= 1
	player.lastmove = 'n_x'
	ontile(False)

#battles
def goblin_battle():
	pre_battle(goblin.name, goblin.hp, goblin.ap, goblin.acc, goblin.spd)
	
def wolf_battle():
	pre_battle(wolf.name, wolf.hp, wolf.ap, wolf.acc, wolf.spd)

def kraken_battle():
	pre_battle(kraken.name, kraken.hp, kraken.ap, kraken.acc, kraken.spd)
	
def crab_battle():
	pre_battle(crab.name, crab.hp, crab.ap, crab.acc, crab.spd)

#get an item
def getitem():
	if (Overworld['land'+str(player.px)+'_'+str(player.py)]['item']) == None:
		print ('there are no items here.')
		go()
	else:
		player_items.append((Overworld['land'+str(player.px)+'_'+str(player.py)]['item']))
		print ('You obtained an item: '+Overworld['land'+str(player.px)+'_'+str(player.py)]['item'])
		(Overworld['land'+str(player.px)+'_'+str(player.py)]['item']) = None
		go()

#get a weapon
def getweapon():
	if (Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']) == None:
		print ('There are no weapons here.')
		go()
	else:
		player.weapon = (Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']).name
		player.ap = (Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']).ap
		player.acc = (Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']).acc
		print ('You obtained a weapon: '+Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon'].name)
		(Overworld['land'+str(player.px)+'_'+str(player.py)]['weapon']) = None
		go()
	
#prebattle menu
def pre_battle(e_race, e_hp, e_ap, e_acc, e_spd):
	looper = True
	t.sleep(1)
	print('The '+e_race+' saw you! Run or fight. (r/f)')
	prebattle_inp = input(inp)
	if prebattle_inp == 'r':
		while looper == True:
			pre_battle_rand = random.randint(1,10)
			if pre_battle_rand <= e_spd:
				print('The '+e_race+' was faster!')
				battle(e_race, e_hp, e_ap, e_acc)
			else:
				print('You ran away!')
				ontile(True)
	elif prebattle_inp == 'f':
		battle(e_race, e_hp, e_ap, e_acc)
	else:
		invalid_inp()
		
# Battle
def battle(e_race, e_hp, e_ap, e_acc):
	turncount = 1

	#enemy turn
	def enemyturn():
		e_hit = random.randint(1,10)
		time.sleep(1)
		print('\nENEMY TURN')
		if e_hit > e_acc:
			print(str(e_race)+' missed!\n')
		else:
			print('The '+str(e_race)+' hit you.\n')
			player.hp -= e_ap						
		print(line)
		t.sleep(1)
						
	print(line+'\nThe '+e_race+' wants to battle!\n'+line)
	while True:
		if player.hp <= 0:
			death()
			break
		elif e_hp <= 0:
			print('you defeatet the '+str(e_race)+'\n')
			ontile(True)
		elif player.hp <= 0 and e_hp <= 0:
			death()
		time.sleep(1)
		print('TURN '+str(turncount))
		turncount += 1
		t.sleep(2)		
		print(line)
		print(str(player.name)+': HP: '+str(player.hp)+' | AP: '+str(player.ap))
		print(str(e_race)+': s HP: '+str(e_hp)+' | AP: '+str(e_ap))
		print(line)
		print('\nYOUR TURN\nDo you want to fight or use a potion? (f/p)')
		battle_inp = input(inp)
		if battle_inp == 'f':
			t.sleep(1)
			punch_hit = random.randint(1,10)
			if punch_hit >= player.acc:
				print('you missed!')
				enemyturn()
			else:
				print('you used your '+player.weapon+'!')
				e_hp -= player.ap
		else:
			invalid_inp()
			turncount -= 1

#this saves game data
def save():
	print ('Do you want to save? This will overwrite your last save. (y/n)')
	save_inp = input(inp)
	if save_inp == 'y':
		saveList = [player.name, player.weapon, player.maxhp, player.hp, player.ap, player.acc, player.px, player.py, player.lastmove]
	elif save_inp =='n':
		go()
	else:
		save()

#death of player
def death():
	print('=========')
	print('YOU DIED!')
	print('=========')
	t.sleep(3)
	lastsave()

def lastsave():
	print ('load from last save? (y/n)')
	afterDeathLoader_inp = input(inp)
	if afterDeathLoader_inp == 'y':
		try:
			player = playable (saveList[0], saveList[1], saveList[2], saveList[3], saveList[4], saveList[5], saveList[6], saveList[7], saveList[8])
			desc()
		except NameError:
			print('No save file found!')
			title()
	elif afterDeathLoader_inp == 'n':
		title()
	else:
		invalid_inp()
		afterDeathLoader_inp()

#shows stats of player
def stats():
	print ('=================')
	print ('palyer stats:')
	print ('HP: '+str(player.hp))
	print ('max HP: '+str(player.maxhp))
	print ('=================')
	print ('weapon stats:')
	print ('weapon: '+player.weapon)
	print ('AP: '+str(player.ap))
	print ('accuracy: '+str(player.acc))
	print ('=================')
	go()

#help
def gamehelp():
	print ('Game commands:\ngo <north/east/south/west>: move <north/east/south/west>\nget item: get the item on the tile\nget weapon: get the weapon on the tile\nstats: see player stats\nsave: save the game\nquit: quit he game\n')
	print ('Difficulties:\neasy: you can save the game.\nhard: yu cannot save the game.')
	menu()

#information about the game
def info():
	print('==================')
	print('Made with Python 3')
	print('Made by Dead Pixel')
	print('==================')
	menu()

#invalid input error
def invalid_inp():
	print('Invalid input! Try again!')

#starting
title()
