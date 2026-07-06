import json
import os
from datetime import datetime

DB_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1

def add_task(tasks):
    title = input("Task: ").strip()
    priority = input("Priority (High/Medium/Low): ").title() or "Medium"
    due = input("Due Date (DD-MM-YYYY or blank): ").strip()
    tasks.append({
        "id": next_id(tasks),
        "title": title,
        "priority": priority,
        "due_date": due,
        "completed": False,
        "created": datetime.now().strftime("%d-%m-%Y %H:%M")
    })
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n------ TASK LIST ------")
    for t in tasks:
        status = "Done" if t["completed"] else "Pending"
        print(f'ID:{t["id"]} | {t["title"]}')
        print(f'Priority: {t["priority"]}')
        print(f'Due: {t["due_date"] or "N/A"}')
        print(f'Status: {status}')
        print("-"*35)

def mark_done(tasks):
    try:
        tid = int(input("Task ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    for t in tasks:
        if t["id"] == tid:
            t["completed"] = True
            save_tasks(tasks)
            print("Task marked completed.")
            return
    print("Task not found.")

def delete_task(tasks):
    try:
        tid = int(input("Task ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    for t in tasks:
        if t["id"] == tid:
            tasks.remove(t)
            save_tasks(tasks)
            print("Task deleted.")
            return
    print("Task not found.")

def search(tasks):
    key = input("Keyword: ").lower()
    found = [t for t in tasks if key in t["title"].lower()]
    if not found:
        print("No matching tasks.")
        return
    for t in found:
        print(f'{t["id"]}: {t["title"]}')

def stats(tasks):
    total=len(tasks)
    done=sum(t["completed"] for t in tasks)
    print(f"Total Tasks : {total}")
    print(f"Completed  : {done}")
    print(f"Pending    : {total-done}")

def menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Statistics")
    print("7. Exit")

def main():
    tasks=load_tasks()
    while True:
        menu()
        choice=input("Enter choice: ")
        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            mark_done(tasks)
        elif choice=="4":
            delete_task(tasks)
        elif choice=="5":
            search(tasks)
        elif choice=="6":
            stats(tasks)
        elif choice=="7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()
