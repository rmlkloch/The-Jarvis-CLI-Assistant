import json
import random
import math

tasks = [] 
contacts = {}
def add_task():
    task_name = input("Assign me a new task:")
    tasks.append(task_name)
    print("Task added.")
    
def show_tasks():
    if len(tasks) == 0:
        print("List is empty.")
    else:
        print("Your Tasks: \n")
        for i in tasks:
            print(f"{i}\n")
            
def add_contact():
    name = input("Enter name: ")
    info = input(f"Enter contact info for {name}: ")
    contacts[name] = info
    print(f"Saved contact: {name}")
    
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved.")
    
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        pass

def get_contact():
    name = input("Who are you looking for? ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")
        
def show_help():
    print("\n--- MENU ---")
    print("add task    : Add a task")
    print("list        : List tasks")
    print("contact add : Add contact")
    print("contact get : Get contact")
    print("quit        : Exit")
    print("calc        : Calculator")
    print("play        : Play a game")
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    
    print("Tasks saved to tasks.txt")
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                clean_task = line.strip()
                tasks.append(clean_task)
                
    except FileNotFoundError:
        pass
    
def play_game():
    target = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == target:
        print("You won!")
    else:
        print(f"Wrong. It was {target}.")
        
def calc():
    while True:
        print("Choose an operation: +, -, *, /, power, sqrt or quit")
        opr = input("Operation: ")
        
        if opr == "quit":
            break

        elif opr == "+":
            total = 0

            while True:
                no = input("Input numbers to calculate, type 'done' after you finish: ")

                if no.lower() == "done":
                    break

                total += float(no)

            print("Sum is:", total)

        elif opr == "-":
            no1 = float(input("First number: "))
            no2 = float(input("Second number: "))
            print("Result is:", no1 - no2)
            
        elif opr == "*":
            x = 1
            while True:
                no = input("Input numbers to calculate, type 'done' after you finish: ")
                
                if no.lower() == "done":
                    break
                
                x *= float(no)
            print("result is", x)
            
        elif opr == "/":
            no1 = float(input("First number: "))
            no2 = float(input("Second number: "))
            print("Result is:", no1 / no2)
            
        elif opr == "power":
            base = float(input("Base: "))
            exp = float(input("Exponent: "))
            print(pow(base, exp))
            
        elif opr == "sqrt":
            no = float(input("Number: "))
            print(math.sqrt(no))

        else:
            print("Invalid operation")
            break

print("Jarvis Online.\n")

load_tasks()
load_contacts()

while True:
    command = input("Tell me what to do, sir: ").lower()

    if command == "quit":
        print("Good Bye sir")
        save_tasks()
        save_contacts()
        break

    elif command == "help":
        show_help()

    elif command == "add task":
        add_task()

    elif command == "list":
        show_tasks()

    elif command == "contact add":
        add_contact()

    elif command == "contact get":
        get_contact()
        
    elif command == "play":
        play_game()
        
    elif command == "calc":
        calc()
        
    else:
        print("I do not understand that command.")