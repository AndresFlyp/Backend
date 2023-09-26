from tu_app.models import Task
from django.contrib.auth.models import User
from django.db.models import Q


def task_filter_priority(prio: str):
    # Filtrar tareas con prioridad "HIGH"
    high_priority_tasks = Task.objects.filter(priority=prio)

def task_filter_user(usuario: str):
    # Filtrar tareas creadas por un usuario específico
    user = User.objects.get(username=usuario)
    user_tasks = Task.objects.filter(user=user)

def task_filter_date(fecha: str):
    # Filtrar tareas completadas en una fecha específica
    date_completed = fecha  # Reemplaza esto con la fecha deseada
    completed_tasks = Task.objects.filter(datecompleted=date_completed)

def try_joins(usuario: str):
    # Utilizar Joins
    tasks_with_username = Task.objects.filter(user__username=usuario)

def task_recent(cantidad: int):
    # Obtener las 5 tareas más recientes
    latest_tasks = Task.objects.order_by('-created')[:cantidad]

def task_most_important():
    # Obtener las 10 tareas más importantes
    high_priority_tasks = Task.objects.filter(priority="HIGH")[:10]

def task_try_Q():
    tasks = Task.objects.filter(Q(priority='HIGH') | Q(priority='MEDIUM'), datecompleted__isnull=False)


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
