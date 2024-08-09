
# Simple Todo List App

<a>
  <img src="https://github.com/VincentRitchie/SIMPLE-APPS/blob/main/Simple%20To%20Do%20List%20in%20Python.jpeg" alt="Logo" width="650" />
</a>

## Table of Contents
- [Description](#description)
- [Pseudocode](#pseudocode)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshot](#screenshot)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Description
This repository contains a simple Python application for managing a to-do list using lists. The application allows users to add, remove, and view tasks.

## Pseudocode

```
pseudocode

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

```

## Features
- **Task Management:** Add and remove tasks from your to-do list.
- **View Tasks:** Display all current tasks in the list.

## Installation
To install and run this project, follow these steps:

```sh
git clone https://github.com/VincentRitchie/Simple-Todo-List-App.git
cd Simple-Todo-List-App
```

## Usage
To use this project, run the following command:

```sh
python todo_list_app.py
```
Follow the prompts to manage your to-do list.

## Screenshot

<a>
  <img src="https://github.com/VincentRitchie/SIMPLE-APPS/blob/main/Todo%20Calc%20Screenshot.png" alt="Logo" width="650" />
</a>

## Future Enhancements

### 1. **User Interface**
   - **Description**: Develop a graphical user interface (GUI) using Tkinter or PyQt to make the application more user-friendly.
   - **Benefit**: Enhances usability by providing a visual interface for users who prefer not to use the command line.

### 2. **Task Persistence**
   - **Description**: Implement functionality to save and load tasks from a file or database.
   - **Benefit**: Allows users to keep their tasks between sessions.

### 3. **Task Prioritization**
   - **Description**: Add support for task prioritization and sorting based on priority.
   - **Benefit**: Helps users manage tasks more effectively by highlighting important tasks.

### 4. **Due Dates and Reminders**
   - **Description**: Allow users to set due dates for tasks and receive reminders.
   - **Benefit**: Improves task management by adding time-based features.

### 5. **Task Categories**
   - **Description**: Add support for categorizing tasks into different groups.
   - **Benefit**: Helps users organize tasks based on different areas of their life.

### 6. **Command-line Arguments**
   - **Description**: Allow users to specify tasks and actions through command-line arguments.
   - **Benefit**: Provides a streamlined way to interact with the application for advanced users.

## Contributing

Feel free to submit issues and enhancement requests. Pull requests are also welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VincentRitchie/SIMPLE-APPS/blob/main/LICENSE) file for details.

## Author

#### Vincent Chimaobi (CyberGhoxt)

Connect with me on 
- [GitHub](https://www.github.com/VincentRitchie/VincentRitchie)
- [LinkedIn](https://www.linkedin.com/in/vincent-chimaobi-53b458216?trk=contact-info)
- [X](https://x.com/vin_chimaobi042)
