# Python CLI To-Do App

A simple command-line to-do list manager built with Python.  
This project demonstrates core Python programming concepts such as file I/O, user input validation, control flow, functions, and error handling.

## Features

- Add new tasks to your to-do list
- View all current tasks with numbered indexing
- Remove tasks by selecting their number
- Persistent storage — tasks are saved to a text file and reloaded on every run
- Input validation for menu choices and task removal
- Error handling for invalid input and missing files

## Technologies Used

- Python 3

## Project Structure

```
python-cli-todo-app
│
├── todo.py
├── tasks.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── todo_example_add.png
    ├── todo_example_view.png
    └── todo_example_remove.png
```

## How to Run

1. Clone the repository:
```
git clone https://github.com/Nstudent1/python-cli-todo-app.git
```

2. Navigate into the project folder:
```
cd python-cli-todo-app
```

3. Run the program:
```
python todo.py
```

> **Note:** A `tasks.txt` file will be created automatically the first time you add a task. You can also include an empty `tasks.txt` in the project folder before running.

## Example Usage

```
Welcome to the To-Do List App!

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Choose an option from 1-4: 1
Enter a new task: Buy groceries
Task 'Buy groceries' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Choose an option from 1-4: 2
----- Your Tasks -----
1. Buy groceries
----------------------
```

## Concepts Demonstrated

- Python functions
- While loops
- File I/O using `open()`, `read()`, and `write()`
- Input validation
- Exception handling using `try` / `except`
- List operations (`append`, `pop`, `enumerate`)
- Basic program structure with a `main()` entry point

## Screenshots

### Adding and Viewing Tasks
![Adding a task](screenshots/todo_example_add.png)

### Viewing Tasks
![Viewing a task](screenshots/todo_example_view.png)

### Removing a Task
![Removing a task](screenshots/todo_example_remove.png)

## Future Improvements

- Add task priority levels (high, medium, low)
- Add due dates to tasks
- Mark tasks as complete without deleting them
- Convert the app into a web application using Flask
- Add a graphical user interface (GUI) using Tkinter
- Add automated tests using `unittest` or `pytest`

## Author

Nicholas D' Rozario
