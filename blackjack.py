import random

suits = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

	def __init__(self, suit, rank):

		self.rank = rank
		self.suit = suit

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))
				
	def __str__(self):
		string = ""
		for card in self.deck:
			string += " " + card.__str__()
		return string
		
	def shuffle(self):
		random.shuffle(self.deck)
	
	def deal(self):
		return self.deck.pop()
		
class Hand:
	
	def __init__(self):
		self.hand = []
		self.sum_of_cards = 0
		self.num_of_aces = 0
	
	def __str__(self):
		return "Hand total: " + str(self.sum_of_cards)
		
	def add_card(self, card):
		#while self.num_of_aces > 0
		self.hand.append(card)
		if card.rank == 'Ace':
			if self.sum_of_cards > 10:
				self.sum_of_cards += 1
				#self.num_of_aces -= 1
		else:		
			self.sum_of_cards += values[card.rank]
	
	def show_hand(self):
		for card in self.hand:
			print(card)
			
class Bankroll:

	def __init__(self, initial_bankroll=100):
		self.bank = initial_bankroll
		self.wager = 0
		
	def __str__(self):
		return "You have: " + str(self.bank)
	
	def wager(self):
	
		while True:
		
			try:
				amount = int(input("How much would you like to wager?"))
			except:
				print("Please input an integer.")
			else:
				if amount > self.bank:
					print("Sorry you do not have enough.")
				else:
					self.wager += amount
					break
		
	def win_wager(self, amount):
		self.bank += self.wager
		return self
		
	def lose_wager(self, amount):
		self.bank -= self.wager
		return self
		
def hit_or_stay (deck, hand):

	while True:
		choice = input("Hit or stay? Enter 'h' for 'Hit', or 's' for 'Stay'\n")
		if choice == 'h':
			hit(deck, player_hand)
			print("Player hand:\n")
			player_hand.show_hand()
			print("\n")
			if player_hand.sum_of_cards > 21:
				print(player_hand)
				print("Sorry, you busted!")
				break
		if choice == 's':
			print("Player hand:\n")
			player_hand.show_hand()
			print(player_hand)
			while house_hand.sum_of_cards < player_hand.sum_of_cards:
				hit(deck, house_hand)
				print("\nHouse hand:\n")
				house_hand.show_hand()
				print("\n")
				if house_hand.sum_of_cards > 21:
					print("You win!")
					break
			if house_hand.sum_of_cards > player_hand.sum_of_cards and house_hand.sum_of_cards < 21:
				print(house_hand)
				print("The House (always) wins!")
			elif house_hand.sum_of_cards == player_hand.sum_of_cards:
				print("It's a tie!")
				break
			break
			
def hit(deck, hand):

	dealt_card = deck.deal()
	hand.add_card(dealt_card)
			
def check_for_winner(player_hand, house_hand):
	if player_hand.sum_of_cards < 21 and player_hand.sum_of_cards > house_hand.sum_of_cards:
		print("You win!")
	elif player_hand.sum_of_cards < 21 and player_hand.sum_of_cards < house_hand.sum_of_cards:
		print("The House (always) wins!")
		

sample_deck = Deck()
sample_deck.shuffle()
#print(sample_deck)
#sample_card = sample_deck.deal()
#print(sample_card)

player_hand = Hand()
house_hand = Hand()

#setup
card = sample_deck.deal()
player_hand.add_card(card)

card = sample_deck.deal()
player_hand.add_card(card)

card = sample_deck.deal()
house_hand.add_card(card)

card = sample_deck.deal()
house_hand.add_card(card)

print("Player hand:\n")
player_hand.show_hand()
print("\n")
print("House hand:\n")
house_hand.show_hand()
print("\n")

hit_or_stay(sample_deck, player_hand)