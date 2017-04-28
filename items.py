class item:
	def __init__ (self, name, effect, desc):
		self.name = name
		self.effect = effect
		self.desc = desc
		
BattleBottle = item('bottle o battle', 'ap_p_p10', 'This bottle with a strange orange fluid makes you permanently stronger by 10 AP.')
HealthShard = item('health shard', 'hp_p_p10', 'This red chrystal shard makes your life energy permanently stronger by 10 HP.')
MagicStone = item('magic stone', None, 'It is useless, but now you can tell EVERYONE that you have a magic stone. How cool is that!')
Cake = item('cake', 'hp_np_p5', 'A moist and soft dessert that replenishes 5 HP')
