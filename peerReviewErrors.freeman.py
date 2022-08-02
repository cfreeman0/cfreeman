# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

#peer review
#July 31st, 2022
#Caleb Freeman
#CIS 245
#I could only find 5 of the errors unless the other 5 were the ones that would come after fixing the 'while' indenditation error in line 20
import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		#1 Line 20 has  indentation error before while
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves
#2 Line 25 has caves when they had it earlier as cave
def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'
		#3Line 43 needs () around the ''.
playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	#5 Line 46 after playAgain there is suppose to be 2 equal signs.
	displayIntro()
	caveNumber = choosecave()
    #4 Line 49 suppose to be chooseCave() not with lowercase c for cave.
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

