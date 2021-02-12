import json
import random
import getpass


def play():
	print("\n==========QUIZ START==========")
	score = 0
   
	with open("C:/Users/chintu/Desktop/Rishitha_quiz/quiz_ques.json", 'r+') as f: # read file of questions
		j = json.load(f)
		for i in range(10): # 10 questions loop
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')

#MAIN PROGRAM STARTS
if __name__ == "__main__":
	choice = 1
	while choice != 0:
		print('\n=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('PRESS 1 TO START QUIZ')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
