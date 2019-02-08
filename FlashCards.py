import re
from random import *
import os

class FlashCard():
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

def Play(cards):
	print("\n\nEnter 'stop' to stop playing\n\n")
	shuffle(cards)	#randomize order of questions

	stop = False;

	for x in range(0, len(cards)):
		if stop != True: 
			print(cards[x].question)
			answer = input("Your answer: ")

			if answer.upper() == cards[x].answer:
				print("You're right!\n")

			elif answer == "stop":
				stop = True

			else:
				print("WRONG! Answer is: " + cards[x].answer + "\n")

		else:
			exit()

question_pattern = "([0-9]+[0-9]*[0-9]*\)(?:.|\n)*?)Answer: "
answer_pattern = "Answer:..(.)"

while True:
	chapter = input("Enter the chapter that you would like to study: ")
	filename = "testbanks/chap" + chapter + ".txt"
	
	if os.path.isfile(filename):
		break

	else:
		print("Chapter not available")

f = open(filename, 'r')
text = f.read()
f.close()

q = re.findall(question_pattern, text)
a = re.findall(answer_pattern, text)
cards = [None]*len(q)

for x in range(0, len(q)):
	cards[x] = FlashCard(q[x], a[x])

Play(cards)