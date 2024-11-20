-----------simple slot machine :

import random 

lines = 3 
column = [0 for _ in range(lines)]
wins = 0

while True : 

   amount = input("Amount of Bet: ")
   if amount.isdigit():
       amount = int(amount)
       if amount <= 0 :
           print("please , Enter a Number Larger than zero")
       else :
           break
   else :
        print("please Enter a Number")

while amount > 0 :

   sym1 = random.randint(1 , 3)
   sym2 = random.randint(1 , 3)
   sym3 = random.randint(1 , 3)

   for _ in column :

       column[0] = sym1
       column[1] = sym2
       column[2] = sym3

   print("You Have " , amount , " Coins in Game")
   ask = input("Would You Want To Play Now or Not  (y/n) : ")
   if ask == "n": 
       print("Game Closed.")
       break
   elif ask == "y" :
       amount -= 1
       print(column)
       if column[0] == column[1] == column[2] :
           print("Nice You Win.")
           wins += 1
           
       else :
           print("oops , You Lose!")
   else :
       print("Please , Choose Between (y/n)")

   if amount == 0 :
       break
