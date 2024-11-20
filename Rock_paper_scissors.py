import random

user_wins = 0
computer_wins = 0
options = ["rock" , "paper" , "scissors"] 
while True :

   user_input = input("Type a rock/paper/scissors or q to quit:\n ")
   if user_input == "q" :
       print("Game Closed.")
       break
   if user_input not in options :
       continue

   random_number = random.randint(0,2)
   computer_pick = options[random_number]

   if user_input == "rock" and computer_pick == "scissors" :

       print("You Win")
       user_wins += 1
   elif user_input == "paper" and computer_pick == "rock" :

       print("You Win")
       user_wins += 1
   elif user_input == "scissors" and computer_pick == "paper" :
       print("You Win")
       user_wins += 1
   elif user_input == computer_pick :
       print("draw")

   else :
       print("You Lose ")
       computer_wins += 1
print("You Win ", user_wins , " Times.")
print("The Computer Wins " , computer_wins , "Times.")
print("Goodbye")
