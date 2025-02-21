
import json
import os
import sys
from datetime import datetime

# Ruta del archivo Json
TASKS_FILE = "tasks.json"

# Función para cargar tareas desde el archivo JSON
def load_task():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        content = file.read()
        if not content:  # Si el contenido está vacío
            return []
        return json.loads(content)

# Función para guardar tareas en el archivo JSON
def save_tasks(task):
    with open(TASKS_FILE, "w") as file:
        json.dump(task, file, indent=4)

# Función para agregar una nueva tarea
def add_task(description):
    tasks = load_task()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAT": datetime.now().isoformat(),
        "updatedAT": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada con éxito (ID: {task_id})")

# Función para actualizar una tarea
def update_task(task_id, new_description):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAT'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Tarea {task_id} actualizada con éxito.')
            return
    print(f'Tarea {task_id} no encontrada.')

# Función para eliminar una tarea  
def delete_task(task_id):
    tasks = load_task()
    # Verificar si la tarea existe
    if not any(task["id"] == task_id for task in tasks):
        print(f"Tarea {task_id} no encontrada.")
        return

    # Compresión de lista para eliminar la tarea
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Tarea {task_id} eliminada con éxito.")

# Función para marcar una tarea como en progreso
def mark_in_progress(task_id):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAT"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarea {task_id} marcada como en progreso.")
            return 
    print(f"Tarea {task_id} no encontrada.")

# Función para marcar una tarea como realizada
def mark_done(task_id):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAT'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Tarea {task_id} marcada como realizada.')
            return
    print(f'Tarea {task_id} no encontrada.')

# Función para listar todas las tareas 
def list_task(status=None):
    tasks = load_task()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Descripción: {task['description']}, Estado: {task['status']}, Creado en: {task['createdAT']}, Actualizado en: {task['updatedAT']}")

# Función principal para manejar comandos
def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona un comando.")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Por favor, proporciona una descripción de la tarea.")
            return
        add_task("".join(sys.argv[2:]))
    elif command == "update":
        if len(sys.argv) < 4:
            print("Por favor, proporciona un ID de tarea y una nueva descripción.")
            return
        update_task(int(sys.argv[2]), ' '.join(sys.argv[3:])) 
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Por favor, proporciona un ID de tarea.")
            return
        delete_task(int(sys.argv[2]))
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Por favor, proporciona un ID de tarea.")
            return
        mark_in_progress(int(sys.argv[2]))
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Por favor, proporciona un ID de tarea.")
            return
        mark_done(int(sys.argv[2]))  
    elif command == 'list':
        if len(sys.argv) == 3:
            list_task(sys.argv[2])
        else:
            list_task()
    else:
               print("Comando desconocido. Por favor, usa add, update, delete, mark-in-progress, mark-done o list.")

if __name__ == '__main__':
    main()