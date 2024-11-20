import sqlite3

db = sqlite3.connect("web.db")
cr = db.cursor()
def commit_close() :

    print("App Closed")
    db.commit()
    db.close()

input_message = """
What Do You Want To Do ?
"s" => show data
"a" => add a new email
"d" => delete your email
"q" => quit the App
"""

user_input = input(input_message).strip().lower()

def show_data() :

    name_input = input("Enter Your Name: ").strip().capitalize()
    email_input = input("Enter Your Email: ").strip()
    cr.execute(f"select * from data where name= '{name_input}' and email= '{email_input}'")
    results = print(cr.fetchall())
    for row in  results :
        print(f"Name: {row[0]}")
        print(f"Email: {row[1]}")
        print(f"Password: {row[2]}")
    
    commit_close()

def add_email():

    name_input = input("Enter Your Name: ").strip().capitalize()
    email_input = input("Enter Your Email: ").strip()
    cr.execute(f"select name,email from data where name = '{name_input}' and email = '{email_input}'")
    result = cr.fetchone()
    if result == None :
        
        password_input = input("Enter Password: ").strip()
        cr.execute(f"insert into data values ('{name_input}' ,'{email_input}' ,'{password_input}')")
        print("Your Email Added")
    else :
        print("Your Email Is Actually Exist")
    commit_close()

def delete_email(): 

    name_input = input("Enter Your Name: ").strip().capitalize()
    email_input = input("Enter Your Email: ").strip()
    cr.execute(f"delete from data where name = '{name_input}' and email= '{email_input}'")
    print("Email Deleted.")
    commit_close()

commands = ["s" , "a" , "d" , "q"]

if user_input in commands :

    print("command found" , user_input)
    if user_input == "s" :
        show_data()
    elif user_input =="a":
        add_email()
    elif user_input == "d" :
        delete_email()
    else :
        commit_close()
else :
    print(f"sorry ,This Command \" {user_input} \" Not Found :(")
