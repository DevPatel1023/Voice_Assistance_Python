import json, os

TODO_FILE = "data/todo.json"

def load_todo():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todo(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def add_task(task: str):
    tasks = load_todo()
    tasks.append({"task": task, "done": False})
    save_todo(tasks)
    return f"Task '{task}' added."

def list_tasks():
    tasks = load_todo()
    if not tasks:
        return "No tasks available."
    return "\n".join([f"[{'✔' if t['done'] else ' '}] {t['task']}" for t in tasks])

def mark_done(task_index: int):
    tasks = load_todo()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_todo(tasks)
        return f"Task {tasks[task_index]['task']} marked as done."
    return "Invalid task number."
