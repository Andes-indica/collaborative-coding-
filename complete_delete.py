from add_view import tasks

def complete_task():
    if not tasks:
        print("No tasks available")
        return

    try:
        task_no = int(input("Enter task number to mark as completed: "))
        index = task_no - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def delete_task():
    if not tasks:
        print("No tasks available")
        return

    try:
        task_no = int(input("Enter task number to delete: "))
        index = task_no - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
