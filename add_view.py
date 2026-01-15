tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available")
        return

    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Pending"
        print(f"{i+1}. {t['task']} [{status}]")
