import random

def newgame():
	choices = ['rock','paper','scissors']
	player = None
	computer = random.choice(choices)
	while player not in choices:
		player = input("rock, paper, scissors: \n")
		player = player.lower()
		comp = print(f"Computer: {computer}")
		play = print(f"Player: {player}")
		if player == computer:
			comp()
			play()
			tie()
		elif player == "rock":
			if computer == "paper":
				comp()
				play()
				lost()
			if computer == "scissors":
				comp()
				play()
				won()
		elif player == "paper":
			if computer == "scissors":
				comp()
				play()
				lost()
			if computer == "rock":
				comp()
				play()
				won()
		elif player == "scissors":
			if computer == "rock":
				comp()
				play()
				lost()
			if computer == "paper":
				comp()
				play()
				won()
def won():
	print("you have won!")
def lost():
	print("You have lost!")
def tie(:
	print("Its a tie!")
def again():
	response = input("Try again? [yes/no]:\n")
	response = response.lower()
	if response == "yes":
		return True
	else:
		return False
newgame()
while again():
	newgame()
