from gestion_tareas.models.task import Task
from gestion_tareas.models.board import Board
from django.contrib.auth.models import User
from django.db.models import Q
# from gestion_tareas.Query import task_filter_priority, task_filter_user, task_filter_date, try_joins, task_recent, task_most_important, task_try_Q, create_tasks, update_tasks, board_filter_month
# from gestion_tareas.Query import board_filter_month

def task_filter_priority(prio: str):
    # Filtrar tareas con prioridad "HIGH"
    high_priority_tasks = Task.objects.filter(priority=prio)
    return high_priority_tasks

    #high_priority_tasks = task_filter_priority("HIGH")
    #print("Tareas con prioridad alta:", high_priority_tasks)

def task_filter_user(usuario: str):
    # Filtrar tareas creadas por un usuario específico
    user = User.objects.get(username=usuario)
    user_tasks = Task.objects.filter(user=user)
    return user_tasks

    # user_tasks = task_filter_user("andres01")
    # print("Tareas del usuario específico:", user_tasks)

def task_filter_date(fecha: str):
    # Filtrar tareas completadas en una fecha específica
    date_completed = fecha  # Reemplaza esto con la fecha deseada
    completed_tasks = Task.objects.filter(datecompleted=date_completed)
    return completed_tasks

def try_joins(usuario: str):
    # Utilizar Joins
    tasks_with_username = Task.objects.filter(user__username=usuario)
    return tasks_with_username

    # joined_tasks = try_joins("andres01")
    # print("Tareas con nombre de usuario:", joined_tasks)

def task_recent(cantidad: int):
    # Obtener las 5 tareas más recientes
    latest_tasks = Task.objects.order_by('-created')[:cantidad]
    return latest_tasks

    # latest_tasks = task_recent(5)
    # print("Las 5 tareas más recientes:", latest_tasks)

def task_most_important():
    # Obtener las 10 tareas más importantes
    high_priority_tasks = Task.objects.filter(priority="HIGH")[:10]
    return high_priority_tasks

    # important_tasks = task_most_important()
    # print("Las 10 tareas más importantes:", important_tasks)

def task_try_Q():
    tasks = Task.objects.filter(Q(priority='HIGH') | Q(priority='MEDIUM'), datecompleted__isnull=False)
    return tasks

    # q_filtered_tasks = task_try_Q()
    # print("Tareas con prioridad 'HIGH' o 'MEDIUM' y fecha completada:", q_filtered_tasks)


def create_tasks():
    # Crea una lista de instancias de Task
    tasks_to_create = [
        Task(title='Tarea 1', description='Descripción 1', priority='HIGH', user_id=1),
        Task(title='Tarea 2', description='Descripción 2', priority='MEDIUM', user_id=2),
        # Agrega más tareas según sea necesario
    ]
    
    # Utiliza bulk_create para crear las tareas de forma masiva
    Task.objects.bulk_create(tasks_to_create)

def update_tasks():
    # Obtén todas las tareas del usuario con ID 1
    tasks_to_update = Task.objects.filter(user_id=1)

    # Actualiza la prioridad de todas las tareas seleccionadas
    tasks_to_update.update(priority='LOW')




def board_filter_month(month:str):
    board_month = Board.objects.filter(month=month)
    return board_month

    #board_month = board_filter_month("DIC")
    #print("Tareas con prioridad alta:", board_month)