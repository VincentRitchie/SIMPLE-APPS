# -----------------------------------------TO DO LIST -----------------------------------------------------
# Declaring an empty list as tasks
tasks = []
# Defining a functon for addding a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")
# Defining a functon for removing a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"{task } Task not found")
# Defining a functon to show tasks on To-Do list
def show_task():
    if not tasks:
        print("ENJOY NO TASK!!!")
    else:
        print("\n TO-DO LIST")
        for task in tasks:
            print(f"- {task}")

# Defining a function for while loop
def main():
    while True:
        # Printing Menu for options selection
        print ("\nOptions")
        print("1: Add Task")
        print("2: Remove Task")
        print("3: Show Tasks")
        print("4: Quit")
        # Enter Your Option Choice
        option = input("Enter Your Option: ")
        # Condition Statement
        if option == '1':
            task= input("Enter Task: ")
            add_task(task)
        elif option == '2':
            task= input("Enter Task: ")
            remove_task(task)
        elif option == '3':
            show_task()
        elif option == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid Option: Please Enter 3 to Show the Manu")
# Run the main function
if __name__ == "__main__":
    main()



