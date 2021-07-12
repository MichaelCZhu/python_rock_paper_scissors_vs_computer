# title and introduction
import random
print("\n")
print("Welcome to Michael's python two player version of rock paper scissors (v2)")
print("\n")
print("Please select one of these three options:")
print("\n")
print("...rock...")
print("...paper...")
print("...scissors...")
print("\n")

#player1 input
print("Enter your choice:")
print("\n")
player1 = input()
print("\n")


#computer ai input
computer_player = random.randint(0,2)

# 0 = rock
# 1 = paper
# 2 = scissors


# beginning of game logic
if player1:

	rock = str("rock")
	big_rock = str("Rock")
	paper = str("paper")
	big_paper = str("Paper")
	scissors = str("scissors")
	big_scissors = str("Scissors")

	print("Rock...Paper...Scissors...SHOOT!")
	print("\n")

	if player1 == rock or player1 == big_rock:
		if computer_player == 0:
			print("Computer played rock.\n\nIt's a TIE. Try again!")
			print("\n")
		elif computer_player == 1:
			print("Computer played paper.\n\nComputer wins!")
			print("\n")
		elif computer_player == 2:
			print("Computer played scissors.\n\nYou win!")
			print("\n")
	elif player1 == paper or player1 == big_paper:
		if computer_player == 0:
			print("Computer played rock.\n\nYou win!")
			print("\n")
		elif computer_player == 1:
			print("Computer played paper.\n\nIt's a TIE. Try again!")
			print("\n")
		elif computer_player == 2:
			print("Computer played scissors.\n\nComputer wins!")
			print("\n")
	elif player1 == scissors or player1 == big_scissors:
		if computer_player == 0:
			print("Computer played rock.\n\nComputer wins!")
			print("\n")
		elif computer_player == 1:
			print("Computer played paper.\n\nYou win!")
			print("\n")
		elif computer_player == 2:
			print("Computer played scissors.\n\nIt's a TIE. Try again!")
			print("\n")
	else:
		print("Something went wrong. Please try again!")
else:
	print("Please input a choice next time!")
	print("\n")