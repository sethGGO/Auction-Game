
import random

class Bot(object):

	def __init__(self):
		self.name = "1966184" # Put your id number her. String or integer will both work
		# Add your own variables here, if you want to. 

	def get_bid_game_type_collection(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids):
		"""Strategy for collection type games. 

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be "collection" for collection type games
		winner_pays(int):				Rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game - will always be 200
		starting_budget(int):			How much budget each bot started with - will always be 1001
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games - will always be [4,2]
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,3,1] means you need 3 of one tpye of painting, 3 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot. 
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far 

		Returns:
		int:Your bid. Return your bid for this round. 
		"""

		# WRITE YOUR STRATEGY HERE FOR COLLECTION TYPE GAMES - FIRST TO COMPLETE A FULL COLLECTION

		print(painting_order[current_round])
		
		money= my_bot_details['budget']
		auction_length = round_limit
		myid= my_bot_details['bot_unique_id']

		def serial_artist(target_collection, artists_and_values, current_round, painting_order, serial):
			auction_length = round_limit
			artist_count = {}
			artist_flag = {}
			for j in artists_and_values.keys():
				artist_flag[j] = 0
				artist_count[j] = 0				
			for i in range(current_round, auction_length):
				if i == auction_length - 1:
					return False
				for artist in artists_and_values.keys():
					# if itemsinauction[i] == artist:
					if artist_flag[artist] == 0 and painting_order[i] == artist:
						artist_count[artist] += 1
						if artist_count[artist] == target_collection[0]:
							# first_artist = artist
							artist_flag[artist] = 1
							count = 0
							for f in artist_flag:
								count += artist_flag[f]
							if count == serial:
								# print('second finish artist')
								return artist
		def serial_artist2(target_collection, artists_and_values, current_round, painting_order, serial):
			auction_length = round_limit
			artist_count = {}
			artist_flag = {}
			for j in artists_and_values.keys():
				artist_flag[j] = 0
				artist_count[j] = 0				
			for i in range(current_round, auction_length):
				if i == auction_length - 1:
					return False
				for artist in artists_and_values.keys():
					# if itemsinauction[i] == artist:
					if artist_flag[artist] == 0 and painting_order[i] == artist:
						artist_count[artist] += 1
						if artist_count[artist] == target_collection[1]:
							# first_artist = artist
							artist_flag[artist] = 1
							count = 0
							for f in artist_flag:
								count += artist_flag[f]
							if count == serial:
								# print('second finish artist')
								return artist
		def ifTwo(vinci_count,picasso_count,rembrandt_count,van_count):
			a=0
			group=[]
			if vinci_count>0:
				a=a+1
				group.append('Da Vinci')
			if picasso_count>0:
				a=a+1
				group.append('Picasso')
			if rembrandt_count>0:
				a=a+1
				group.append('Rembrandt')
			if van_count>0:
				a=a+1
				group.append('Van Gogh')
			return group
		vinci_count= my_bot_details["paintings"]["Da Vinci"]
		picasso_count= my_bot_details["paintings"]["Picasso"]		
		rembrandt_count= my_bot_details["paintings"]["Rembrandt"]
		van_count= my_bot_details["paintings"]["Van Gogh"]
		gr= ifTwo(vinci_count,picasso_count,rembrandt_count,van_count)
		art =serial_artist(target_collection, artists_and_values, current_round, painting_order, 1)
		print(str(art)+ ' no1')

		for player in bots:
			if player["paintings"][painting_order[current_round]] == target_collection[0]-1 and player['bot_unique_id'] != myid:
				print('hihi2')
				if painting_order[current_round] not in gr:
					print(myid)
					print('hihi3')
					print(my_bot_details['budget'])
					print(player['budget'] + 1)
					if my_bot_details['budget'] > player['budget'] + 1:
						return player['budget'] + 1
					if my_bot_details['budget'] == player['budget'] :
						return player['budget']
					print('opt1')
				if painting_order[current_round] in gr:
					if my_bot_details['budget'] > player['budget'] + 1:
						return player['budget'] + 1


		if myid in winner_ids:
			vinci_count= my_bot_details["paintings"]["Da Vinci"]
			picasso_count= my_bot_details["paintings"]["Picasso"]		
			rembrandt_count= my_bot_details["paintings"]["Rembrandt"]
			van_count= my_bot_details["paintings"]["Van Gogh"]

			gr= ifTwo(vinci_count,picasso_count,rembrandt_count,van_count)

			if len(gr)==1:
				myartist = painting_order[winner_ids.index(myid)]

				first = serial_artist2(target_collection, artists_and_values, current_round, painting_order, 1)
				second = serial_artist2(target_collection, artists_and_values, current_round, painting_order, 2)
				third = serial_artist2(target_collection, artists_and_values, current_round, painting_order, 3)
				if painting_order[current_round] == myartist and my_bot_details['paintings'][myartist]<target_collection[0]:
					print('opt21')
					return int(money / (target_collection[0]+target_collection[1] - my_bot_details['paintings'][myartist]))
				elif painting_order[current_round] != myartist and (first == painting_order[current_round] or second == painting_order[current_round]) :
					one= first
					print(str(one)+' one')
					return int(money / (target_collection[0]+target_collection[1]- my_bot_details['paintings'][myartist]))
				else:
					return 0
			if len(gr)>=2:
				myartists= gr
				if painting_order[current_round] in myartists:
					print('itsinart')
					myartist = painting_order[winner_ids.index(myid)]
					if my_bot_details['paintings'][painting_order[current_round]]<target_collection[0]:
						pos = myartists.index(painting_order[current_round])
						if pos ==0:
							position = 1
						if pos ==1:
							position = 0
						if pos ==2:
							return 0
						if my_bot_details['paintings'][myartists[position]]<=target_collection[1] and my_bot_details['paintings'][painting_order[current_round]]==target_collection[1]:
							z = serial_artist([int(target_collection[0]/2),target_collection[1]], {k: artists_and_values[k] for k in (myartists[0],myartists[1])}, current_round, painting_order, 1)
							if z == painting_order[current_round]:
								print('qazzqq')
								return int(money / (target_collection[0]+target_collection[1] - (my_bot_details['paintings'][myartists[0]]+my_bot_details['paintings'][myartists[1]])))
							else:
								print('qazz')
								return 0
						if my_bot_details['paintings'][myartists[position]]==target_collection[0] and my_bot_details['paintings'][painting_order[current_round]]<target_collection[1]:
							print('getstuck1')
							return int(money / (target_collection[0]+target_collection[1] - (my_bot_details['paintings'][myartists[0]]+my_bot_details['paintings'][myartists[1]])))
						if my_bot_details['paintings'][myartists[position]]>target_collection[1] and my_bot_details['paintings'][painting_order[current_round]]==target_collection[1]:
							print('problemss')
							return 0
										
						return int(money / (target_collection[0]+target_collection[1] - (my_bot_details['paintings'][myartists[0]]+my_bot_details['paintings'][myartists[1]])))


					print('opt21')
					print('getstuck2')
					return 0
				else:
					return 0

		if myid not in winner_ids:
			print('opt3')
			# the first winning list type
			first = serial_artist(target_collection, artists_and_values, current_round, painting_order, 1)
			second = serial_artist(target_collection, artists_and_values, current_round, painting_order, 2)
			third = serial_artist(target_collection, artists_and_values, current_round, painting_order, 3)
			one = ''
			two = ''
			if painting_order[current_round] == first:
				print('opt31')
				one= first
				print(str(one)+' one')
				return int(money / (target_collection[0]+target_collection[1]))+1
			if painting_order[current_round] == second:
				two = painting_order[current_round]
				print(str(two)+' two')
				print('opt31')
				return int(money / (target_collection[0]+target_collection[1]))+1
			else:
				print('opt32')
				return 0


	def get_bid_game_type_value(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids):
		"""Strategy for value type games. 

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be either "collection" or "value", the two types of games we will play
		winner_pays(int):				rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game
		starting_budget(int):			How much budget each bot started with
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,3,1] means you need 3 of one type of painting, 3 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot. 
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far 

		Returns:
		int:Your bid. Return your bid for this round. 
		"""
		# WRITE YOUR STRATEGY HERE FOR VALUE GAMES - MOST VALUABLE PAINTINGS WON WINS
		totalValue = 0
		myid= my_bot_details['bot_unique_id']
		for art in painting_order:
			totalValue += artists_and_values[art]
		

		# Make sure to keep track of what the maximum and minimum value bounds we shouldn't pass over
		upperValueCap = int(totalValue/2)+1
		lowerValueCap = int(totalValue/len(bots))+1


		money= my_bot_details['budget']
		auction_length = round_limit
		myid= my_bot_details['bot_unique_id']
		all_value = 0
		
		for art in painting_order:
			all_value += artists_and_values[art]

		remain_value = 0

		for i in range(current_round, auction_length):
			remain_value += artists_and_values[painting_order[i]]

		myvalue = 0
		for art in artists_and_values:
			myvalue += my_bot_details["paintings"][art] * artists_and_values[art]

		numberbidders = len(bots)
		if numberbidders == 2:
			target = (all_value/numberbidders) + 1
			remain_target = remain_value/numberbidders
		else:
			target = all_value/numberbidders*1.2
			remain_target = remain_value/numberbidders*1.2

		# be more restraint at first, focus on the target
		if remain_value > target - myvalue:
			bid = int(money * artists_and_values[current_painting] / remain_target)
		# try to spend all money averagely
		else:
			bid = int(money * artists_and_values[current_painting] / (remain_value/numberbidders))
		print(bid)
		return bid
		# Here is an example of how to get the current painting's value
		#current_painting_value = artists_and_values[current_painting]
		#print("The current painting's value is ", current_painting_value)

		# Here is an example of printing who won the last round
		#if current_round>1:
		#	who_won_last_round = winner_ids[current_round-1]
		#	print("The last round was won by ", who_won_last_round)

		# Play around with printing out other variables in the function, 
		# to see what kind of inputs you have to work with
		#my_budget = my_bot_details["budget"]
		#return random.randint(0, my_budget)

