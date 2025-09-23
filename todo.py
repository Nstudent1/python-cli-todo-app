print("Welcome to the To-Do List App!\n")

def load_tasks():
    todo_list = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass
    return todo_list

def save_tasks(todo_list):
    with open("tasks.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    save_tasks(todo_list)
    print(f"Task '{task}' added.")

def view_task(todo_list):
    if not todo_list:
        print("No tasks in the list.")
        return

    print("----- Your Tasks -----")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print("----------------------\n")

def remove_task(todo_list):
    view_task(todo_list)
    if not todo_list:
        return
    
    try:
        task_index = int(input("Enter the task number to remove: "))
        if 1 <= task_index <= len(todo_list):
            removed_task = todo_list.pop(task_index - 1)
            save_tasks(todo_list)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option from 1-4: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_task(todo_list)
        elif choice == "3":
            remove_task(todo_list)
        elif choice == "4":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


    

        

