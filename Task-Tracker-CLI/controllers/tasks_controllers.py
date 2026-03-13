from models.tasks_models import Tasks,Database
from views.tasks_views import TasksView

class TaskController:

    @staticmethod
    def add_task(task : str):
        """Create a new task !"""
        try:
            id_task = Tasks.add(task)
            TasksView.diplay_add_task(id_task)
            return id_task

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def update_task(id_task : str,new_task:str):
        """Update a task !"""
        try:
            id_task = Tasks.update(id_task,new_task)
            TasksView.display_update_task(id_task)
            return id_task

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def delete_task(id_task: str):
        """Delete a task !"""
        try:
            id_task = Tasks.delete(id_task)
            TasksView.display_delete_task(id_task)
            return id_task

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def mark_task(id_task: str,new_status: str):
        """Mark a task !"""
        try:
            result = Tasks.mark_task(id_task,new_status)
            TasksView.display_mark_task(result[0],result[1])
            return result[0],result[1]

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def list_all_task():
        """List all of tasks"""
        try:
            tasks = Tasks.list_all_tasks()
            TasksView.display_all_tasks(tasks)
            return tasks

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def list_all_task_done():
        """List all tasks done"""
        try:
            tasks = Tasks.list_all_tasks_done()
            TasksView.display_all_tasks(tasks)
            return tasks

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def list_all_task_todo():
        """List all tasks to do !"""
        try:
            tasks_todo = Tasks.list_all_tasks_todo()
            TasksView.display_list_all_tasks_todo(tasks_todo)
            return tasks_todo

        except Exception as e:
            TasksView.display_error(e)
            return None

    @staticmethod
    def list_all_task_in_progress():
        """List all tasks to do !"""
        try:
            tasks_in_progress = Tasks.list_all_tasks_in_progress()
            TasksView.display_list_all_tasks_in_progress(tasks_in_progress)
            return tasks_in_progress

        except Exception as e:
            TasksView.display_error(e)
            return None
def main():
    pass

if __name__ == '__main__':
    main()