"""
URL configuration for ticsocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestion_tareas.views import signup_view
from gestion_tareas.views import task_view
from gestion_tareas.views import home_view
from gestion_tareas.views import signout_view 
from gestion_tareas.views import signin_view
from gestion_tareas.views import board_view
from gestion_tareas.views.api_task_view import TaskListCreateView, TaskDetailView


urlpatterns = [
    

    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('gestion_tareas.urls'), name='api'),
    path('', home_view.home, name='home'),

    path('signup/', signup_view.signup, name='signup'),
    path('signin/', signin_view.signin, name='signin'),
    path('logout/', signout_view.signout, name='logout'),

    path('tasks_completed/', task_view.tasks_completed, name='tasks_completed'),
    path('create_task/', task_view.create_task, name='create_task'),
    path('tasks/', task_view.tasks, name='tasks'),
    path('tasks/<int:task_id>', task_view.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', task_view.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', task_view.delete_task, name='delete_task'),

    path('boards/',board_view.BoardsView.as_view(), name='boards'),
    path('boards/<int:pk>/',board_view.BoardsView.as_view(), name='board_detail'),

    path('tasks_api/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks_api/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

]
