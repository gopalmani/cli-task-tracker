import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

#Creating/initialising a json file if it does not exists
def create_task_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)

#Reading file
def read_task_file():
    with open(TASKS_FILE, 'r') as f:
        json.load(f)

#writing task 
def write_task(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

#Generate unique id
def generate_unique_id(tasks):
    if not isinstance(tasks, list):
        tasks = []
    return max([task.get('id', 0) for task in tasks], default=0) + 1
    
#Add task
def add_task(desc):
    tasks = read_task_file() or []
    task = {
        'id' : generate_unique_id(tasks),
        'desc' : desc,
        'status' : 'To-Do',
        'createdAt' : datetime.now().isoformat(),
        'updatedAt' : datetime.now().isoformat()

    }
    tasks.append(task)
    write_task(tasks)
    print(f"TASK ADDED : {task}")

#Update task
def update_task(task_id, status):
    tasks = read_task_file()
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            write_task(tasks)
            print(f"TASK UPDATED✅: {task}")
            return
        print("TASK NOT FOUND⚠️")

#Delete task
def delete_task(task_id):
    tasks = read_task_file
    tasks = [task for task in tasks if task['id'] != int(task_id)]
    write_task(tasks)

#List task
def list_task(filter_status = None):
    tasks = read_task_file()
    for task in tasks:
        if filter_status is None or task['status'] == filter_status:
            print(task)

#CLI HANDLING

def main():
    create_task_file()

    if len(sys.argv) < 2:
        print("Usage : python task_tracker.py <command. [<argv>]")
        return
    
    command = sys.argv[1]

    if command == 'add':
        desc = ' '.join(sys.argv[2:])
        add_task(desc)
    
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py update <task_id> <status>")
            return
        update_task(sys.argv[2], sys.argv[3])
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage Python task_tracker.py delete <task_id>")
        delete_task(sys.argv[2])
    
    elif command == 'list':
        list_task()

    elif command == 'list-done':
        list_task('done')
    
    elif command == 'list-todo':
        list_task('to-do')

    elif command == 'list-in-progress':
        list_task('in-progress')
    
    else:
        print("UNKNOWN COMMAND 〠")

if __name__ == '__main__':
    main()

















