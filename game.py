
# Game Jam Game Oct 2014
# For SESA Game Jam II
#
# By Glen Robertson
#
#
# Theme: Postmodern
#  - skeptical interpretations of culture, fiction, economics, etc
#  - deconstructionist / post structuralist thought
#  - self referential
# Things: 2 ** 32, a credit card, a CD
# 
# 
# To run: python3 game.py
# Probably best not to read the code first!












# NO! Don't go looking at the code!



















# Really, you should play it first!














# Ok fine you probably just wanted to cheat anyway :(


import code

__cc_balance__ = 0
# __cds_produced__ = 0
__cds_in_stock__ = 0
__cd_demand__ = 0


said_words = set()
def say_if_unsaid(words):
	if words not in said_words:
		print(words)
	said_words.add(words)

class Game:


	def __init__(self):
		global __cc_balance__
		global __cds_in_stock__
		global __cd_demand__
		self.__cc_balance__ = 0
		self.cc_balance = 0
		__cc_balance__ = 0
		self.__cds_in_stock__ = 0
		__cds_in_stock__ = 0
		# __cds_produced__ = 0
		__cd_demand__ = 0
		# self.__cds_produced__ = 0
		self.__cd_demand__ = 100

	def start(self):
		game = Game()
		print('Welcome to music manager 0.001')
		say_if_unsaid('Maybe you should try making some cash money')
		# print('You have a credit card with a balance of {}'.format(self.cc_balance))
		print('To see available commands, type commands()')

	def status(self):
		self.__correct_cheating__()
		print('Credit card balance: {}'.format(self.__cc_balance__))
		print('CDs in stock: {}'.format(self.__cds_in_stock__))
		self.__check_win_loss__()
		say_if_unsaid("Wouldn't it be nice to have $2^32?")


	def __check_win_loss__(self):
		if self.__cc_balance__ >= 2 ** 32:
			print('You now have all the money in the world, you win!')
			exit()
		if self.__cc_balance__ > 2 ** 20:
			say_if_unsaid('You are quite the virtual CD baron.')
		if self.__cc_balance__ <= -2 ** 32:
			print('The bank has you assassinated as a last resort, you lose!')
			exit()
		if self.__cc_balance__ < -2 ** 20:
			say_if_unsaid('The bank is a little worried about your balance...')
			

	def __correct_cheating__(self, diff=0, cd_diff=0, demand_diff=0):
		if self.__is_cheating__():
			print('Nice try, you cheater!')
		global __cc_balance__
		global __cds_in_stock__
		global __cd_demand__
		# global __cds_produced__
		self.__cc_balance__ = self.cc_balance = __cc_balance__ = min(self.__cc_balance__, self.cc_balance, __cc_balance__) + diff
		self.__cds_in_stock__ = __cds_in_stock__ = min(self.__cds_in_stock__, __cds_in_stock__) + cd_diff
		self.__cd_demand__ = __cd_demand__ = min(self.__cd_demand__, __cd_demand__) + demand_diff


	def __is_cheating__(self):
		return not (self.__cc_balance__ == self.cc_balance == __cc_balance__ and \
			self.__cds_in_stock__ == __cds_in_stock__ and \
			self.__cd_demand__ == __cd_demand__)

	def produceCDs(self, num=10):
		say_if_unsaid('you can specify number of cds. default is 10. CDs cost $1 to produce')
		self.__correct_cheating__(-num, num)
		# self.__cds_produced__ += num
		# __cds_produced__ += num
		print('Produced {} CDs. You now have {} CDs'.format(num, self.__cds_in_stock__))
		self.__check_win_loss__()

	def __calc_qty__(self, price):
		if price <= 0:
			return 2 ** 64
		return max(self.__cd_demand__, 0) / price

	def sellCDs(self, price=1):
		say_if_unsaid('you can specify the price. default is $1')
		self.__correct_cheating__()
		if self.__cds_in_stock__ <= 0:
			print('You have no CDs to sell! Produce some first!')
			return
		
		qty_demanded = int(self.__calc_qty__(price))
		sold = int(min(self.__cds_in_stock__, qty_demanded))
		self.__correct_cheating__(price * sold, -sold, -sold)
		print('Sold {} CDs at ${} each'.format(sold, price))
		self.__check_win_loss__()

	def advertiseCDs(self, amount=10):
		say_if_unsaid('you can specify the amount to spend, default is 10')
		self.__correct_cheating__(-amount, 0, amount)
		print('Spent ${} on advertising CDs'.format(amount))
		self.__check_win_loss__()
		

game = Game()

__olddir__ = dir
def commands(arg=game):
	print(list(filter(lambda name: not name.startswith('__'), __olddir__(arg))))
	print('Use game.commandname() to run them')
dir = commands


help = 'Try running commands()'


welcome_msg = 'Welcome! This is technically a game, but only just.\n'
welcome_msg += 'It is kinda just Python :D\n'
welcome_msg += 'Use ctrl-D to exit (or ctrl-Z-Z on windows)\n'
welcome_msg += 'Use python commands as you see fit.\n\n'
welcome_msg += 'To begin, try running game.start()'
code.interact(welcome_msg, local=locals())
