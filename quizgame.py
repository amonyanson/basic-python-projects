import time
def line():
	print("---------------------------------------")
def newgame():
	guesses = []
	questionnum = 0
	correctguesses = 0
	for key in questions:
		time.sleep(0.5)
		print(key)
		for i in options[questionnum]:
			time.sleep(0.5)
			print(i)
			line()
		time.sleep(1)
		guess = input("Enter: [A, B, C, D]: \n")
		line()
		guess = guess.upper()
		guesses.append(guess)
		correctguesses += checkanswer(questions.get(key),guess)
		questionnum += 1
	displayscore(correctguesses, guesses)
def checkanswer(answer, guess):
	if answer == guess:
		time.sleep(1)
		print("Corect")
		line()
		return 1
	else:
		time.sleep(2)
		print("Wrong")
		line()
		return 0
def displayscore(correctguesses, guesses):
	time.sleep(3)
	print("Results:\n")
	time.sleep(1)
	print("Answer: \n", end=" ")
	for key in questions:
		time.sleep(0.5)
		print(questions.get(key),end=" ")
	time.sleep(1)
	print("\nGuesses: \n",end=" ")
	for i in guesses:
		time.sleep(1)
		print(i,end=" ")
	time.sleep(1)
	score = int(correctguesses/len(questions)*100)
	time.sleep(1)
	line()
	print(f"\nYour score is: {score}%")
	time.sleep(1)
	if score == 100:
		time.sleep(2)
		print("Great job!\nGrade A")
	elif score == 75:
		time.sleep(3)
		print("Good Job!\nGrade B")
	elif score == 50:
		time.sleep(3)
		print("Ei oyaaaa!!\nGrade C")
	elif score == 25:
		time.sleep(4)
		print("Weh, okay\nGrade D")
	else:
		time.sleep(3)
		print("Yayee, YOu hvae scored an E!!!!!")
def again():
	response = input("Try again?:[yes/no]: \n")
	response = response.lower()
	if response == "yes":
		return True
	else:
		return False

questions = {
	"Who created python?": "A",
	"In what year was python created?": "B",
	"Python is tributed to which comedy group?": "C",
	"Which is the greatest programming language of all time": "D"
}
options = [
	["A. Guido Van rossum","B. Elon MUsk","C. Jeff BEzos","D. MArk ZUckerburg"],
	["A. 1990","B. 1991","C. 1992","D. 1993"],
	["A. Cracked Python","B. The Dark Asset","C. Monty Python","D. Pirates of teh caribbean"],
	["A. Javascript","B. PHP","C. HTML","D. Python"]
]
newgame()
while again():
	newgame()