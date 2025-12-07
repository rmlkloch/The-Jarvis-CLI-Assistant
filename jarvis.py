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

print("Jarvis Online.\n")

load_tasks()

while True:
    command = input("Tell me what to do, sir: ").lower()

    if command == "quit":
        print("Good Bye sir")
        save_tasks()
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
        
    else:
        print("I do not understand that command.")