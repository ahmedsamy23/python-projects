import random

top_of_range = input("type a Number: ")

if top_of_range.isdigit() :
   top_of_range = int(top_of_range)

   if top_of_range <= 0 :
       print("Please Enter a Number larger than 0 in Next Time!")
       quit()
else :
       print("please type a number")
       quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True :

   guesses += 1
   user_guess = input("Guess a Number: ")
   if user_guess.isdigit() :
       user_guess = int(user_guess)
   else :
       print("please type a number next time")
       continue

   if user_guess == random_number :
       print("Correct You Got it!")
       break
   elif user_guess > random_number :
       print("You were above The Number")
   else :
       print("You Were Below The Number")
   
print("You Got it in " , guesses , "guesses")
