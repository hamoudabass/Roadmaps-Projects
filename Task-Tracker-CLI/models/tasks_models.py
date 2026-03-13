import json
import os
from typing import Any
import datetime


class Database:
    def __init__(self, database=r"C:\Users\HP\Desktop\RoadMap Project\Task Tracker\data/task.json"):
        self.database = database
        self.charger_donnees()

    def charger_donnees(self):

        if not os.path.exists(self.database):
            data = {"tasks": {}}
            self.sauvegarder_donnees(data)
            return data

        try:
            with open(self.database, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Si le fichier est vide ou corrompu
            data = {"tasks": {}}
            self.sauvegarder_donnees(data)
            return data

    def sauvegarder_donnees(self, data):
        with open(self.database, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

class DateTask:

    @staticmethod
    def create_at():

        now = datetime.datetime.now()
        now_time = now.strftime('%H:%M:%S')
        now_date = datetime.datetime.now().strftime('%d-%m-%Y')

        return f"{now_time}"

    @staticmethod
    def finish_at():
        tdelta = datetime.timedelta(hours=5)
        now = datetime.datetime.now()
        expiretime = now + tdelta
        expire_time = expiretime.strftime('%H:%M:%S')

        return expire_time

class Tasks :

    @staticmethod
    def add(task: str) -> str:
        db : Database = Database()
        data = db.charger_donnees()

        numbers = [
            int(task_id)
            for task_id in data["tasks"].keys()
            if task_id.isdigit()
        ]

        id_task = str(max(numbers, default=0) + 1)



        data["tasks"][id_task] = {
            "name": task,
            "status": "todo",
            "create_at": DateTask.create_at(),
            "finish_at": DateTask.finish_at()
        }

        db.sauvegarder_donnees(data)
        return id_task

    @staticmethod
    def update(id_task: str, new_task: str) -> str:

        db: Database = Database()
        data = db.charger_donnees()

        if id_task not in data["tasks"]:
            return "Task not found!"

        task_status = data["tasks"][id_task]["status"]

        data["tasks"][id_task] = {
            "name": new_task,
            "status": task_status,
            "create_at": DateTask.create_at(),
            "finish_at": DateTask.finish_at()
        }

        db.sauvegarder_donnees(data)

        return id_task

    @staticmethod
    def delete(id_task) -> str:

        db: Database = Database()
        data = db.charger_donnees()

        if id_task not in data["tasks"]:
            return "Task not found!"

        tasks = data['tasks']
        tasks.pop(id_task)

        db.sauvegarder_donnees(data)

        return id_task

    @staticmethod
    def mark_task(id_task: str,new_status: str) -> list[str] | str:

        db: Database = Database()
        data = db.charger_donnees()

        if id_task not in data["tasks"]:
            return "Task not found!"

        task_name = data["tasks"][id_task]["name"]

        data["tasks"][id_task] = {
            "name": task_name,
            "status": new_status,
            "create_at": DateTask.create_at(),
            "finish_at": DateTask.finish_at()
        }

        db.sauvegarder_donnees(data)

        return [id_task,new_status]

    @staticmethod
    def list_all_tasks() -> list[Any]:

        db: Database = Database()
        data = db.charger_donnees()
        tasks = []

        for id_task in data["tasks"].keys():
            name_task = data["tasks"][id_task]["name"]
            status = data["tasks"][id_task]["status"]
            create_at = data["tasks"][id_task]["create_at"]
            finish_at = data["tasks"][id_task]["finish_at"]
            task = id_task, name_task, status, create_at,finish_at
            tasks.append(task)
        return tasks

    @staticmethod
    def list_all_tasks_done() -> list[str]:

        db: Database = Database()
        data = db.charger_donnees()
        all_tasks = data["tasks"].items()
        tasks_done = []

        for id_task, task_desc in all_tasks:
            for desc in task_desc.values():
                if "done" in desc:
                    name_task = data["tasks"][id_task]["name"]
                    status = data["tasks"][id_task]["status"]
                    create_at = data["tasks"][id_task]["create_at"]
                    finish_at = data["tasks"][id_task]["finish_at"]
                    task = id_task, name_task, status, create_at, finish_at
                    tasks_done.append(task)
        return tasks_done

    @staticmethod
    def list_all_tasks_todo() -> list[str]:

        db: Database = Database()
        data = db.charger_donnees()
        all_tasks = data["tasks"].items()
        tasks_todo = []

        for id_task, task_desc in all_tasks:
            for desc in task_desc.values():
                if "todo" in desc:
                    name_task = data["tasks"][id_task]["name"]
                    status = data["tasks"][id_task]["status"]
                    create_at = data["tasks"][id_task]["create_at"]
                    finish_at = data["tasks"][id_task]["finish_at"]
                    task = id_task, name_task, status, create_at, finish_at
                    tasks_todo.append(task)
        return tasks_todo

    @staticmethod
    def list_all_tasks_in_progress() -> list[str]:

        db: Database = Database()
        data = db.charger_donnees()
        all_tasks = data["tasks"].items()
        tasks_in_progress = []

        for id_task, task_desc in all_tasks:
            for desc in task_desc.values():
                if "in progress" in desc:
                    name_task = data["tasks"][id_task]["name"]
                    status = data["tasks"][id_task]["status"]
                    create_at = data["tasks"][id_task]["create_at"]
                    finish_at = data["tasks"][id_task]["finish_at"]
                    task = id_task, name_task, status, create_at, finish_at
                    tasks_in_progress.append(task)
        return tasks_in_progress

def menu():
    print(Tasks.list_all_tasks())

if __name__ == '__main__':
    menu()
