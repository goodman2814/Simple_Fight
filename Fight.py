#Fighting Game Idea
#THis will be a "simple" text based fighting game.
#A player will enter 'punch', 'kick', 'dodge', or 'counter' 
#computer will choose 'punch', 'kick', 'dodge', or 'counter'  
#resolve the clash with comp and or play losing a hit point.
#game ends when someones hit points reach zero


from random import randint

print("The fight begins. You may punch or kick your oppnent and try to dodge or counter their attack. Who will win?")
print()

playerHP = 10 
compHP = 10

# create a while loop to keep the game going
while playerHP > 0 and compHP > 0:
	# Establish HP 
	print()
	print(f"Player HP: {playerHP}   Computer HP: {compHP}")
	print()
	#retrieve playe move
	player = input("Player, make your move. Do you punch, kick, dodge, or counter? ").lower()

	#exit code
	if player == "quit" or player == "q":
		break

	

	#establish computer move
	rand_num = randint(0,4)

	if rand_num == 0:
		comp = "punch"
	elif rand_num == 1:
		comp = "kick"
	elif rand_num == 2:
		comp = "dodge"
	else:
		comp = "counter"

	#resolve attacks
	if player == 'punch':
		if comp == 'punch':
			print('The computer swung its fists!')
			print('Both players take damage!')
			playerHP-=1 
			compHP-=1
		elif comp == 'kick':
			print('The computer strikes with its foot!')
			print('Both players take damage!')
			playerHP-=2 
			compHP-=1
		elif comp == 'counter':
			print("The computer countered your attack!")
			print('You take damage!')
			playerHP-=1
		else:
			print('The computer dodged your attack!')
			print('You miss!')

	if player == 'kick':
		if comp == 'punch':
			print('The computer swung its fists!')
			print('Both players take damage!')
			playerHP-=1 
			compHP-=2
		elif comp == 'kick':
			print('The computer strikes with its foot!')
			print('Both players take damage!')
			playerHP-=2 
			compHP-=2
		elif comp == 'counter':
			print("The computer countered your attack!")
			print('You take damage!')
			playerHP-=2
		else:
			print('The computer dodged your attack!')
			print('You miss!')

	elif player == 'counter':
		if comp == 'punch':
			print(f"The computer tried to {comp} you!")
			print("You countered the computer's attack!")
			print('The computer takes damage!')
			compHP-=1
		elif comp == 'kick':
			print(f"The computer tried to {comp} you!")
			print("You countered the computer's attack!")
			print('The computer takes damage!')
			compHP-=2
		elif comp == 'dodge':
			print('The computer dodged your attack!')
			print('You miss!')
		elif comp == 'counter':
			print('You both feint a counter!')
			print('No damage!')

	elif player == 'dodge':
		print("You dodged the computer's attack! They miss!")


	# else:
	# 	if player != 'punch' or 'kick' or 'counter' or 'dodge':
	# 		print('Please enter a valid command.')

if playerHP > 0:
	print()
	print("RESULT:")
	print(f"Player HP: {playerHP}   Computer HP: {compHP}")
	print()
	print("CONGRATULATIONS! PLAYER WINS!")
elif player_wins == comp_wins:
	print("DRAW!!")
else:
	print()
	print("RESULT:")
	print(f"Player HP: {playerHP}   Computer HP: {compHP}")
	print()
	print("FAILURE! COMPUTER WINS!")
