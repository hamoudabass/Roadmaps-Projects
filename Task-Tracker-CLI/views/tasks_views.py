class TasksView :

    @staticmethod
    def display_tasks(task):
        """Afficher les details d'une tache"""
        if task :
            print(f"\n{'=' * 50}")
            print(f"ID: {task[0]}")
            print(f"Nom: {task[1]}")
            print(f"Status: {task[2]}")
            # print(f"Crée à: {task[3]}")
            # print(f"Expire à: {task[4]}")
            print(f"{'=' * 50}\n")
        else:
            print("Tache non trouvée !")

    @staticmethod
    def display_all_tasks(tasks):
        """Affiche tous les taches !"""

        if not tasks:
            print("Aucun tâche enregistré")
            return
        print(f"\n{'=' * 80}")
        print(f"{'ID':<5} {'Nom':<30} {'Status':<10} {'Crée le':<15}{'Expire le':<15}")
        print(f"{'=' * 80}")

        for task in tasks:

            print(f"{task[0]:<5} {task[1]:<30} {task[2]:<10} {task[3]:<15} {task[4]:<15}")

        print(f"\n{'=' * 80}")

    @staticmethod
    def diplay_add_task(id_task):
        print(f"Task added successfully (ID: {id_task})")

    @staticmethod
    def display_update_task(id_task):
        print(f"Task updated successfully (ID: {id_task})")

    @staticmethod
    def display_delete_task(id_task):
        print(f"Task deleted successfully (ID: {id_task})")

    @staticmethod
    def display_mark_task(id_task,new_status):
        print(f"Task (ID: {id_task}) new status:{new_status}")

    @staticmethod
    def display_list_all_tasks_done(tasks_done):
        """Affiche tous les taches finies"""

        print(f"\n{'=' * 80}")
        if not tasks_done:
            print("Aucun tâche finie enregistré")
            return

        print(f"\n{'=' * 80}")
        print(f"{'ID':<5} {'Nom':<30} {'Status':<10} {'Crée le':<15}{'Expire le':<15}")
        print(f"{'=' * 80}")

        for task in tasks_done:
            print(f"{task[0]:<5} {task[1]:<30} {task[2]:<10} {task[3]:<15} {task[4]:<15}")

        print(f"\n{'=' * 80}")

    @staticmethod
    def display_list_all_tasks_todo(tasks_todo):
        """Affiche tous les taches à faire"""

        print(f"\n{'=' * 80}")
        if not tasks_todo:
            print("Aucun tâche à faire enregistré")
            return

        print(f"\n{'=' * 80}")
        print(f"{'ID':<5} {'Nom':<30} {'Status':<10} {'Crée le':<15}{'Expire le':<15}")
        print(f"{'=' * 80}")

        for task in tasks_todo:
            print(f"{task[0]:<5} {task[1]:<30} {task[2]:<10} {task[3]:<15} {task[4]:<15}")

        print(f"\n{'=' * 80}")

    @staticmethod
    def display_list_all_tasks_in_progress(tasks_in_progress):
        """Affiche tous les taches en cours"""

        print(f"\n{'=' * 80}")
        if not tasks_in_progress:
            print("Aucun tâche en cours enregistré")
            return

        print(f"\n{'=' * 80}")
        print(f"{'ID':<5} {'Nom':<30} {'Status':<10} {'Crée le':<15}{'Expire le':<15}")
        print(f"{'=' * 80}")

        for task in tasks_in_progress:
            print(f"{task[0]:<5} {task[1]:<30} {task[2]:<10} {task[3]:<15} {task[4]:<15}")

        print(f"\n{'=' * 80}")


    @staticmethod
    def display_success(message):
        """Affiche un message de succès"""
        print(f"\n✓ {message}\n")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur"""
        print(f"\n✗ Erreur: {message}\n")

def main():
    pass

if __name__ == '__main__':
    main()



