# -----------------------------------------TO DO LIST ------------------------------------------------------
"""
Initialize tasks as an empty list

Define function add_task(task):
    Append task to tasks list
    Print "Added task: task"

Define function remove_task(task):
    If task is in tasks list:
        Remove task from tasks list
        Print "Removed task: task"
    Else:
        Print "Task not found: task"

Define function show_tasks():
    If tasks list is empty:
        Print "No tasks in the list."
    Else:
        Print "To-Do List:"
        For each task in tasks:
            Print "- task"

Define function main():
    Loop infinitely:
        Print menu options (1. Add task, 2. Remove task, 3. Show tasks, 4. Quit)
        Get user input for choice

        If choice is '1':
            Prompt user to enter a task
            Call add_task(task)
        Else if choice is '2':
            Prompt user to enter a task
            Call remove_task(task)
        Else if choice is '3':
            Call show_tasks()
        Else if choice is '4':
            Print "Exiting the to-do list application."
            Break the loop
        Else:
            Print "Invalid choice. Please choose a valid option."

Call main() to run the application


"""
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



