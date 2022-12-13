import random

endGame = False
win = False
maxFailedAttempts = 6
turns = 0
failedAttempts = 0
lettersFound = []
lettersNotInWord = []

# Create a list with all words
with open("wordlist.txt", "r") as allWordsFile:
	allWords = allWordsFile.read().splitlines()

# Choose a random word
randomWord = random.choice(allWords).lower()
print(("_ " * len(randomWord)).rstrip())
print()

while not endGame:
	letter = input("Please enter a letter: ")
	while len(letter) != 1:
		letter = input("Invalid input, please try again: ")

	if letter in lettersNotInWord or letter in lettersFound:
		print("You have already attempted this letter.")
		continue
	print()

	success = randomWord.find(letter) > -1
	if success:
		lettersFound += letter
		print("You found a letter!")
	else:
		failedAttempts += 1
		lettersNotInWord += letter
		print("Your letter is not in the word.")
		print(f"Failed Attempts: {failedAttempts}/{maxFailedAttempts}")
		
	for char in randomWord:
		if char in lettersFound:
			print(char, end=" ")
		else:
			print("_", end=" ")
	print()
	print(f"Letters Found: {', '.join(lettersFound)}")
	print(f"Incorrect Letters: {', '.join(lettersNotInWord)}")
	print()
	if failedAttempts >= maxFailedAttempts:
		turns += 1
		win = False
		endGame = True

print("The game has ended.")

# Win/Loose Logic
if win:
	print("Congratulations! You found the word.")
	print(f"It was '{randomWord}'")
else:
	print("You Lost!")
	with open("deadman.txt", "r") as deadmanFile:
		print(deadmanFile.read())
	print("Failed Attempts:", failedAttempts, "/", maxFailedAttempts)
	print(f"The word was '{randomWord}'")
	print("Better luck next time!")
