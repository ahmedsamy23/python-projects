class stack :

   def __init__(self) : 

       self.tasks = []

   def add_task(self , task):
       
       self.tasks.append(task)

   def remove_task(self):

       remove = int(input("Enter The Task You Want to Remove (by Number): "))
       try :
           if 1 <= remove <= len(self.tasks) :
               self.tasks.pop(remove - 1)
               print("task has removed")
           else : 
               print("the task number is invalid")
       except ValueError :
           print("please enter a number")
   
   def show_tasks(self):
       if self.is_Empty():
           print("There are no Tasks in The List")

       for i , task in enumerate(self.tasks , 1):
            print(f"{i}- {task}")


   def is_Empty(self) :

       if len(self.tasks) == 0 :
           print("There are no Tasks in The List")

def tasks_list() :

   s = stack()

   while True : 

       still = input("You Want to Still in The Application (y/n)? ").lower()
       if still == "n" :
           print("App Closed")
           break
       elif still == "y" :
           while True :
               """
               Hello in Senor Application 

               What do you Want to Do :
               Add Task -> add
               Show Tasks -> show
               Remove task -> remove
               """
               ask = input("""
               Hello in Senor Application 

               What do you Want to Do :
               Add Task -> add
               Show Tasks -> show
               Remove task -> remove
               close app -> q
               """).lower()

               if ask == "add" :
                   task = input("Enter the task: \n")
                   s.add_task(task)
               elif ask == "show" :
                   s.show_tasks()
               elif ask == "remove" :
                   s.remove_task()
               elif ask == "q" :
                   with open("to_do_list.txt","a") as t :
                       for j , task in enumerate(s.tasks , 1):
                           line = f"{j}- {task} \n"
                           t.write(line)
                                                   
                   print("App closed")
                   break
               else : 
                   print("Invalid input, Try again")
                   continue

       else : 
           print("please enter y or n ")
           continue



tasks_list()
