# coding=utf-8

from app import components
from app.tasks.model import Task


class TaskService(components.Service):
    _model_class = Task

    def __init__(self):
        super().__init__()


taskService = TaskService()


class Module(components.Module):
    from app.tasks.controller import TaskListController, TaskController
    name = "tasks"
    services = [taskService]
    models = [Task]
    controller = [TaskController, TaskController]


module = Module()
