import json


def load_tasks():
    with open("data/tasks.json", 'r') as file:
        cur_tasks = json.load(file)

    return cur_tasks


def save_tasks(tasks):
    with open("data/tasks.json", 'w') as file:
        json.dump(tasks, file)


def add_task(data: dict) -> str:

    if "intent" in data:
        del data["intent"]

    cur_tasks = load_tasks()

    cur_tasks["tasks"].append(data)

    with open("data/tasks.json", 'w') as file:
        json.dump(cur_tasks, file)

    return f"Successfully added '{data['task_name']}', due {data['due_date']} to database."


def remove_task(data: dict) -> str:
    data.pop("intent", None)

    cur_tasks = load_tasks()

    if not cur_tasks.get("tasks"):
        return "No tasks to remove."

    task_date = data.get("task_date")
    if not task_date:
        return "Missing task date."

    new_tasks = {
        "tasks": [
            task for task in cur_tasks["tasks"]
            if task.get("due_date") != task_date
        ]
    }

    save_tasks(new_tasks)

    return "Successfully removed task."


def list_tasks() -> str:

    response = ["Your current tasks include the following:"]

    tasks = load_tasks()["tasks"]

    if len(tasks) == 0:
        return "No tasks to display."

    for task in load_tasks()["tasks"]:
        response.append(
            f"{task['task_name']}, created at {task["created_at"]}, due: {task["due_date"]}")

    return "\n".join(response)
